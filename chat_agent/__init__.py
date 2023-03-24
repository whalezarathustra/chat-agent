import os

from chat_agent.config import config_helper

# agent
CHAT_HOST_KEY = 'CHAT_AGENT_HOST'
CHAT_PORT_KEY = 'CHAT_AGENT_PORT'
CHAT_AGENT_SECRET_KEY = 'CHAT_AGENT_SECRET_KEY'

CHAT_AGENT_HOST_DEFAULT = '0.0.0.0'
CHAT_AGENT_PORT_DEFAULT = 8080
CHAT_AGENT_SECRET_KEY_DEFAULT = os.urandom(24)

CHAT_AGENT_HOST = config_helper.get_config_from_env(CHAT_HOST_KEY, CHAT_AGENT_HOST_DEFAULT)
CHAT_AGENT_PORT = config_helper.get_config_from_env(CHAT_PORT_KEY, CHAT_AGENT_PORT_DEFAULT)
CHAT_AGENT_SECRET_KEY = config_helper.get_config_from_env(CHAT_AGENT_SECRET_KEY, CHAT_AGENT_SECRET_KEY_DEFAULT)
