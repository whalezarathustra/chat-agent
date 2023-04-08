import json
import threading
import time

import websocket


def on_message(ws, message):
    print("Received message: {}".format(message))


def on_error(ws, error):
    print("Error occurred: {}".format(error))


def on_close(ws, status, msg):
    print("WebSocket connection closed")


def on_open(ws):
    print("WebSocket connection opened")

    def run():
        while True:
            message_data = {
                'message_key': 'websocket_chat',
                'data': json.dumps({'data': 'hello'})
            }
            data = json.dumps(message_data)
            ws.send(data)
            time.sleep(5)
        ws.close()

    threading.Thread(target=run).start()


if __name__ == '__main__':
    server_url = "ws://127.0.0.1:9080"  # Replace with your actual WebSocket server address
    ws = websocket.WebSocketApp(server_url,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.on_open = on_open
    ws.run_forever()
