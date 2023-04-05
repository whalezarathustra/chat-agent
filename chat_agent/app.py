import os
import sys

import eventlet
from flask import Flask, Response, request, send_from_directory, session
from flask_cors import CORS
from flask_socketio import send, SocketIO

from chat_agent import CHAT_AGENT_PORT, CHAT_AGENT_HOST, CHAT_AGENT_SECRET_KEY, CHAT_AGENT_HTTPS, \
    CHAT_AGENT_SSL_CERT_FILE_FULL_PATH, CHAT_AGENT_SSL_KEY_FILE_FULL_PATH, CHAT_AGENT_HTTPS_PORT, \
    CHAT_AGENT_STATIC_PATH, CHAT_AGENT_TIMEOUT
from chat_agent.handler.openai_handler import send_chat_message_with_steam_response
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util import random
from chat_agent.util.context import get_thread_context
from util.timeout import TimeoutError, timeout_decorator

app = Flask(__name__, static_folder=CHAT_AGENT_STATIC_PATH)
socketio = SocketIO(app)
app.config['SECRET_KEY'] = CHAT_AGENT_SECRET_KEY
CORS(app)

logger = get_logger('app')


@app.route('/')
def index():
    sid = get_thread_context()['sid']
    ip = get_thread_context()['remote_ip']
    logger.debug('new guest, sid: {} ip: {}'.format(sid, ip))
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/chat')
@timeout_decorator(CHAT_AGENT_TIMEOUT)
def chat():
    try:
        msg = request.args.get('msg', '')
        chat_log = request.args.get('chat_log', [])
        return Response(send_chat_message_with_steam_response(msg=msg, chat_log=chat_log), content_type='text/plain')
    except TimeoutError:
        return Response('Timeout', content_type='text/plain'), 408


@app.route('/.<path:hidden_path>')
def ssl_check(hidden_path):
    return send_from_directory(app.static_folder, f'.{hidden_path}')


@app.before_request
def before():
    if 'sid' not in session:
        sid = random.get_random_md5()
        session['sid'] = sid
    sid = session['sid']
    get_thread_context()['sid'] = sid
    get_thread_context()['remote_ip'] = request.remote_addr


@socketio.on('websock_chat')
def websock_chat():
    try:
        msg = request.args.get('msg', '')
        chat_log = request.args.get('chat_log', [])
        for message in send_chat_message_with_steam_response(msg=msg, chat_log=chat_log):
            send(message)
    except TimeoutError:
        return Response('Timeout', content_type='text/plain'), 408


def start_agent():
    path = os.path.dirname(sys.argv[0])
    logger.debug('cur static path is: ' + path + '/' + CHAT_AGENT_STATIC_PATH)
    if CHAT_AGENT_HTTPS:
        app.run(
            host=CHAT_AGENT_HOST,
            port=CHAT_AGENT_HTTPS_PORT,
            ssl_context=(CHAT_AGENT_SSL_CERT_FILE_FULL_PATH, CHAT_AGENT_SSL_KEY_FILE_FULL_PATH)
        )
    else:
        app.run(
            host=CHAT_AGENT_HOST,
            port=CHAT_AGENT_PORT
        )


def start_socket_agent():
    eventlet.wsgi.server(eventlet.listen(('', CHAT_AGENT_PORT)), app)


if __name__ == '__main__':
    start_socket_agent()
