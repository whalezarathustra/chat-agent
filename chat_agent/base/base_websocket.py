import json
from collections import OrderedDict

from geventwebsocket import WebSocketServer, WebSocketApplication, Resource
from geventwebsocket.handler import WebSocketHandler

from chat_agent.base.singleton import Singleton
from chat_agent.logger.logger_helper import get_logger
from chat_agent.util.context import get_thread_context
from chat_agent.util.random import get_random_md5

logger = get_logger('base_websocket')


class BaseWebSocket(WebSocketApplication):

    def __init__(self, ws):
        super().__init__(ws)
        self.sid = get_random_md5()
        self.server = BaseWebSocketServer()
        self.remote_addr = ws.environ['REMOTE_ADDR']
        self.remote_port = ws.environ['REMOTE_PORT']

    def get_sid(self):
        return self.sid

    def on_open(self):
        self.server.handle_connect(self)

    def on_message(self, message: str):
        if message is not None:
            self.server.handle_message(self, message)

    def on_close(self, reason):
        self.server.handle_disconnect(self)

    def send_message(self, message):
        self.ws.send(message)


def send_message(message_key, message):
    context = get_thread_context()
    if 'socket' not in context:
        return False
    socket = context['socket']
    message_data = {
        'sid': socket.get_sid(),
        'message_key': message_key,
        'data': message
    }
    data = json.dumps(message_data)
    socket.send_message(data)


def get_remote_ip():
    context = get_thread_context()
    if 'socket' not in context:
        return None
    socket = context['socket']
    return socket.remote_addr


class CustomWebSocketHandler(WebSocketHandler):
    def handle_one_response(self):
        try:
            super(CustomWebSocketHandler, self).handle_one_response()
        except Exception as e:
            logger.error("捕获到异常：{}".format(e))


@Singleton
class BaseWebSocketServer:

    def __init__(self, *args, **kwargs):
        self.sockets = {}
        self.handlers = {}

    def handle_message(self, socket: BaseWebSocket, message: str):
        message_info = json.loads(message)
        message_key = message_info['message_key']
        get_thread_context()['socket'] = socket
        del message_info['message_key']
        self._handle_event(message_key, **message_info)

    def handle_connect(self, socket: BaseWebSocket):
        self.sockets[socket.get_sid()] = socket
        get_thread_context()['socket'] = socket
        if 'connect' in self.handlers:
            self._handle_event('connect')
        logger.debug('handle_connect, sid: {}'.format(socket.get_sid()))

    def handle_disconnect(self, socket: BaseWebSocket):
        del self.sockets[socket.get_sid()]
        if 'disconnect' in self.handlers:
            self._handle_event('disconnect')
        logger.debug('handle_disconnect, sid: {}'.format(socket.get_sid()))

    def _handle_event(self, message_key: str, **kwargs):
        try:
            if message_key not in self.handlers:
                return
            self.handlers[message_key](**kwargs)
        except Exception as e:
            logger.error('hand event has exception, {}'.format(e))

    def on(self, message_key: str):
        def decorator(handler):
            self.handlers[message_key] = handler
            return handler

        return decorator

    def start(self, host: str = '0.0.0.0', port: int = 9080):
        WebSocketServer(
            (host, port),
            Resource(OrderedDict([('/', BaseWebSocket)])),
            handler_class=CustomWebSocketHandler
        ).serve_forever()


if __name__ == '__main__':
    server = BaseWebSocketServer()


    @server.on("websocket_chat")
    def say_hello(data):
        logger.debug('receive message,', data)
        send_message("websocket_chat", "nice to meet you")


    server.start()
