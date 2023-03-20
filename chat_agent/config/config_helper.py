import os


def get_config_from_env(config_key: str, default=None):
    if os.getenv(config_key):
        return os.getenv(config_key)
    else:
        return default
