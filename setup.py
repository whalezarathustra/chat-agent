from setuptools import setup, find_packages

setup(
    name="chat_agent",
    version="0.1.6.5",
    packages=find_packages(),
    zip_sage=False,
    include_package_data=True,
    install_requires=[
        'setuptools~=63.4.1',
        'flask~=2.2.2',
        'flask_cors~=3.0.10',
        'openai~=0.27.2',
        'tiktoken~=0.3.2',
        'bidict~=0.22.1',
        'flask-socketio~=5.3.3',
        'python-engineio~=4.4.0',
        'python-socketio~=5.8.0',
        'python-engineio~=4.4.0',
        'python-socketio~=5.8.0',
        'gevent==22.10.2',
        'gevent-websocket==0.10.1',
        'eventlet==0.33.3'
    ],
    author="WhaleZarathustra",
    author_email="whale.zarathustra@gmail.com",
    description="A Simple Chat Agent, For OpenAI ChatGPT",
    license="MIT",
    keywords="ChatAgent",
    url="https://github.com/whalezarathustra/chat-agent",
)
