CHAT_LOG = 'chat_log'

mock_memory_cache = {
    CHAT_LOG: []
}


def get_cache(key: str):
    return mock_memory_cache[key]


def save_cache(key: str, data):
    mock_memory_cache[key] = data
