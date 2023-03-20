import openai

from chat_agent.config import config_helper

# open api
ORGANIZATION_KEY = 'OPENAI_ORGANIZATION_KEY'
API_KEY = 'OPENAI_API_KEY'
CHAT_ROUND_KEY = 'OPENAI_CHAT_ROUND'
CHAT_TOKEN_MAX_KEY = 'OPENAI_CHAT_TOKEN_MAX'
HISTORY_TOKEN_MAX_KEY = 'OPENAI_HISTORY_TOKEN_MAX'
MODEL_KEY = 'OPENAI_MODEL'
TEMPERATURE_KEY = 'OPENAI_TEMPERATURE'

CHAT_TOKEN_MAX_DEFAULT = 2048
HISTORY_TOKEN_MAX_DEFAULT = 2048
ROUND_DEFAULT = 3
TEMPERATURE_DEFAULT = 0.7
MODEL_DEFAULT = 'gpt-3.5-turbo'

openai.organization = config_helper.get_config_from_env(ORGANIZATION_KEY)
openai.api_key = config_helper.get_config_from_env(API_KEY)
CHAT_ROUND = config_helper.get_config_from_env(CHAT_ROUND_KEY, ROUND_DEFAULT)
CHAT_TOKEN_MAX = config_helper.get_config_from_env(CHAT_TOKEN_MAX_KEY, CHAT_TOKEN_MAX_DEFAULT)
HISTORY_TOKEN_MAX = config_helper.get_config_from_env(HISTORY_TOKEN_MAX_KEY, HISTORY_TOKEN_MAX_DEFAULT)
MODEL = config_helper.get_config_from_env(MODEL_KEY, MODEL_DEFAULT)
TEMPERATURE = config_helper.get_config_from_env(TEMPERATURE_KEY, TEMPERATURE_DEFAULT)
