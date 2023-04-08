import os


def get_config_from_env(config_key: str, default=None):
    if os.getenv(config_key):
        return os.getenv(config_key)
    else:
        return default


def get_boolean_config_from_env(config_key: str, default=None):
    val = get_config_from_env(config_key, default)
    if (isinstance(val, bool) and val) or 'True' == val or 'true' == val:
        return True
    else:
        return False


def get_int_config_from_env(config_key: str, default=None):
    val = get_config_from_env(config_key, default)
    if isinstance(val, str):
        return int(val)
    else:
        return val
