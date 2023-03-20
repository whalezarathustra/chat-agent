from chat_agent.config import config_helper

# agent
CHAT_PORT_KEY = 'CHAT_AGENT_PORT'

CHAT_AGENT_PORT_DEFAULT = 8080

CHAT_GENT_PORT = config_helper.get_config_from_env(CHAT_PORT_KEY, CHAT_AGENT_PORT_DEFAULT)
