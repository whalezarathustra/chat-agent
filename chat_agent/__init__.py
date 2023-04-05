import os

from chat_agent.config import config_helper

# agent
CHAT_AGENT_HOST_KEY = 'CHAT_AGENT_HOST'
CHAT_AGENT_PORT_KEY = 'CHAT_AGENT_PORT'
CHAT_AGENT_HTTPS_PORT_KEY = 'CHAT_AGENT_HTTPS_PORT'
CHAT_AGENT_WEBSOCKET_PORT_KEY = 'CHAT_AGENT_WEBSOCKET_PORT'
CHAT_AGENT_WEBSOCKET_WSS_PORT_KEY = 'CHAT_AGENT_WEBSOCKET_WSS_PORT'
CHAT_AGENT_SECRET_KEY = 'CHAT_AGENT_SECRET_KEY'
CHAT_AGENT_HTTPS_KEY = 'CHAT_AGENT_HTTPS'
CHAT_AGENT_SSL_CERT_FILE_FULL_PATH_KEY = 'CHAT_AGENT_SSL_CERT_FILE_FULL_PATH'
CHAT_AGENT_SSL_KEY_FILE_FULL_PATH_KEY = 'CHAT_AGENT_SSL_KEY_FILE_FULL_PATH'
CHAT_AGENT_STATIC_PATH_KEY = 'CHAT_AGENT_STATIC_PATH'
CHAT_AGENT_TIMEOUT_KEY = 'CHAT_AGENT_TIMEOUT'

CHAT_AGENT_HOST_DEFAULT = '0.0.0.0'
CHAT_AGENT_PORT_DEFAULT = 8080
CHAT_AGENT_HTTPS_PORT_DEFAULT = 8443
CHAT_AGENT_WEBSOCKET_PORT_DEFAULT = 9080
CHAT_AGENT_WEBSOCKET_WSS_PORT_DEFAULT = 9443
CHAT_AGENT_SECRET_KEY_DEFAULT = os.urandom(24)
CHAT_AGENT_HTTPS_DEFAULT = False
CHAT_AGENT_SSL_CERT_FILE_FULL_PATH_DEFAULT = 'cert.pem'
CHAT_AGENT_SSL_KEY_FILE_FULL_PATH_DEFAULT = 'key.pem'
CHAT_AGENT_STATIC_PATH_DEFAULT = 'static'
CHAT_AGENT_TIMEOUT_DEFAULT = 30

CHAT_AGENT_HOST = config_helper.get_config_from_env(CHAT_AGENT_HOST_KEY, CHAT_AGENT_HOST_DEFAULT)
CHAT_AGENT_PORT = config_helper.get_config_from_env(CHAT_AGENT_PORT_KEY, CHAT_AGENT_PORT_DEFAULT)
CHAT_AGENT_HTTPS_PORT = config_helper.get_config_from_env(CHAT_AGENT_HTTPS_PORT_KEY, CHAT_AGENT_HTTPS_PORT_DEFAULT)
CHAT_AGENT_WEBSOCKET_PORT = config_helper.get_config_from_env(CHAT_AGENT_WEBSOCKET_PORT_KEY,
                                                              CHAT_AGENT_WEBSOCKET_PORT_DEFAULT)
CHAT_AGENT_WEBSOCKET_WSS_PORT = config_helper.get_config_from_env(CHAT_AGENT_WEBSOCKET_WSS_PORT_KEY,
                                                                  CHAT_AGENT_WEBSOCKET_WSS_PORT_DEFAULT)
CHAT_AGENT_SECRET_KEY = config_helper.get_config_from_env(CHAT_AGENT_SECRET_KEY, CHAT_AGENT_SECRET_KEY_DEFAULT)
CHAT_AGENT_HTTPS = config_helper.get_boolean_config_from_env(CHAT_AGENT_HTTPS_KEY, CHAT_AGENT_HTTPS_DEFAULT)
CHAT_AGENT_SSL_CERT_FILE_FULL_PATH = config_helper.get_config_from_env(CHAT_AGENT_SSL_CERT_FILE_FULL_PATH_KEY,
                                                                       CHAT_AGENT_SSL_CERT_FILE_FULL_PATH_DEFAULT)
CHAT_AGENT_SSL_KEY_FILE_FULL_PATH = config_helper.get_config_from_env(CHAT_AGENT_SSL_KEY_FILE_FULL_PATH_KEY,
                                                                      CHAT_AGENT_SSL_KEY_FILE_FULL_PATH_DEFAULT)
CHAT_AGENT_STATIC_PATH = config_helper.get_config_from_env(CHAT_AGENT_STATIC_PATH_KEY, CHAT_AGENT_STATIC_PATH_DEFAULT)
CHAT_AGENT_TIMEOUT = config_helper.get_config_from_env(CHAT_AGENT_TIMEOUT_KEY, CHAT_AGENT_TIMEOUT_DEFAULT)
