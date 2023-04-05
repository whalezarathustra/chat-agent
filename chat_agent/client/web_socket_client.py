import json

import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("已连接到服务器")


@sio.event
def disconnect():
    print("已断开与服务器的连接")


@sio.event
def websocket_chat(data):
    print("收到消息:", data)


def main():
    sio.connect('http://127.0.0.1:9080/')

    while True:
        try:
            message = input("输入消息: ")
            request_msg = {"sid": "1", "data": message}
            request_data = json.dumps(request_msg)
            sio.emit('websocket_chat', request_data)
        except KeyboardInterrupt:
            break

    sio.disconnect()


if __name__ == '__main__':
    main()
