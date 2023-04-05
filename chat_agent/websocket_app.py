import json

import eventlet
from eventlet import wsgi
from flask import Flask, request, send_from_directory, session
from flask_cors import CORS
from flask_socketio import emit, SocketIO

from chat_agent import CHAT_AGENT_SECRET_KEY, CHAT_AGENT_STATIC_PATH, \
    CHAT_AGENT_SSL_CERT_FILE_FULL_PATH, CHAT_AGENT_SSL_KEY_FILE_FULL_PATH, CHAT_AGENT_HOST, CHAT_AGENT_HTTPS, \
    CHAT_AGENT_WEBSOCKET_PORT, CHAT_AGENT_WEBSOCKET_WSS_PORT
from chat_agent.handler.openai_handler import send_chat_message_with_socket_steam_response
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util import random
from chat_agent.util.context import get_thread_context, set_thread_context

app = Flask(__name__, static_folder=CHAT_AGENT_STATIC_PATH)
socketio = SocketIO(app, cors_allowed_origins="*")
app.config['SECRET_KEY'] = CHAT_AGENT_SECRET_KEY
CORS(app)

logger = get_logger('websocket_app')


@app.route('/')
def index():
    sid = get_thread_context()['sid']
    ip = get_thread_context()['remote_ip']
    logger.debug('new guest, sid: {} ip: {}'.format(sid, ip))
    return send_from_directory(app.static_folder, 'websocket_index.html')


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


@socketio.on('connect')
def handle_connect():
    if 'sid' not in session:
        sid = random.get_random_md5()
        session['sid'] = sid
    sid = session['sid']
    get_thread_context()['sid'] = sid
    get_thread_context()['remote_ip'] = request.remote_addr
    logger.info('客户端已连接, sid: {} ip: {}'.format(sid, request.remote_addr))


@socketio.on('disconnect')
def handle_disconnect():
    sid = get_thread_context()['sid']
    logger.info('客户端已断开连接, sid: {}'.format(sid))
    set_thread_context(None)


@socketio.on('websocket_chat')
def websock_chat(msg):
    request_msg = json.loads(msg)
    if 'sid' in request_msg:
        session['sid'] = request_msg['sid']
    for response_message in send_chat_message_with_socket_steam_response(msg=request_msg['data'], chat_log=None):
        emit('websocket_chat', response_message, broadcast=True)


def start_socket_agent():
    if CHAT_AGENT_HTTPS:
        ssl_options = {
            'certfile': CHAT_AGENT_SSL_CERT_FILE_FULL_PATH,
            'keyfile': CHAT_AGENT_SSL_KEY_FILE_FULL_PATH
        }
        listener = eventlet.listen((CHAT_AGENT_HOST, CHAT_AGENT_WEBSOCKET_WSS_PORT))
        wsgi.server(eventlet.wrap_ssl(listener, **ssl_options), app)
    else:
        listener = eventlet.listen((CHAT_AGENT_HOST, CHAT_AGENT_WEBSOCKET_PORT))
        wsgi.server(listener, app)


if __name__ == '__main__':
    start_socket_agent()
