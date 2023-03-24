from setuptools import setup, find_packages

setup(
    name="chat_agent",
    version="0.1.3",
    packages=find_packages(),
    zip_sage=False,
    include_package_data=True,
    install_requires=[
        'setuptools~=63.4.1',
        'flask~=2.2.2',
        'flask_cors~=3.0.10',
        'openai~=0.27.2',
        'tiktoken~=0.3.2'
    ],
    author="WhaleZarathustra",
    author_email="whale.zarathustra@gmail.com",
    description="A Simple Chat Agent, For OpenAI ChatGPT",
    license="MIT",
    keywords="ChatAgent",
    url="https://github.com/whalezarathustra/chat-agent",
)
