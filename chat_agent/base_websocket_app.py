import json

from chat_agent import CHAT_AGENT_HOST, CHAT_AGENT_WEBSOCKET_PORT
from chat_agent.base.base_websocket import BaseWebSocketServer, send_message, get_remote_ip
from chat_agent.handler.openai_handler import send_chat_message_with_socket_steam_response
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util import random
from chat_agent.util.context import get_thread_context, set_thread_context

logger = get_logger('websocket_app')

server = BaseWebSocketServer()


@server.on('connect')
def handle_connect():
    sid = random.get_random_md5()
    context = get_thread_context()
    context['sid'] = sid
    context['remote_ip'] = get_remote_ip()
    logger.info('客户端已连接, sid: {} ip: {}'.format(sid, get_remote_ip()))


@server.on('disconnect')
def handle_disconnect():
    sid = get_thread_context()['sid']
    logger.info('客户端已断开连接, sid: {}'.format(sid))
    set_thread_context(None)


@server.on('websocket_chat')
def websock_chat(data):
    context = get_thread_context()
    request_msg = json.loads(data)
    if 'sid' in request_msg:
        context['sid'] = request_msg['sid']
    else:
        sid = random.get_random_md5()
        context['sid'] = sid
    for response_message in send_chat_message_with_socket_steam_response(msg=request_msg['data'], chat_log=None):
        send_message('websocket_chat', response_message)


def start_socket_agent():
    server.start(CHAT_AGENT_HOST, CHAT_AGENT_WEBSOCKET_PORT)


if __name__ == '__main__':
    start_socket_agent()
