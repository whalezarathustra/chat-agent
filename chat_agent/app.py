from flask import Flask, Response, request, send_from_directory, session
from flask_cors import CORS

from chat_agent import CHAT_AGENT_PORT, CHAT_AGENT_HOST, CHAT_AGENT_SECRET_KEY
from chat_agent.handler.openai_handler import send_chat_message_with_steam_response
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util import random
from chat_agent.util.context import get_thread_context

app = Flask(__name__)
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
def chat():
    msg = request.args.get('msg', '')
    chat_log = request.args.get('chat_log', [])
    return Response(send_chat_message_with_steam_response(msg=msg, chat_log=chat_log), content_type='text/plain')


@app.before_request
def before():
    if 'sid' not in session:
        sid = random.get_random_md5()
        session['sid'] = sid
    sid = session['sid']
    get_thread_context()['sid'] = sid
    get_thread_context()['remote_ip'] = request.remote_addr


def start_agent():
    app.run(
        host=CHAT_AGENT_HOST,
        port=CHAT_AGENT_PORT
    )


if __name__ == '__main__':
    start_agent()
