from flask import Flask, Response, request, send_from_directory
from flask_cors import CORS

from chat_agent import CHAT_GENT_PORT
from chat_agent.handler.openai_handler import send_chat_message_with_steam_response

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


@app.route('/chat')
def chat():
    msg = request.args.get('msg', '')
    chat_log = request.args.get('chat_log', [])
    return Response(send_chat_message_with_steam_response(msg=msg, chat_log=chat_log), content_type='text/plain')


def start_agent():
    app.run(
        port=CHAT_GENT_PORT
    )


if __name__ == '__main__':
    start_agent()
