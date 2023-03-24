from threading import Timer

from chat_agent.cache import CACHE_CHAT_LOG_EXPIRE
from chat_agent.util.time import get_timestamp

CHAT_LOG = 'chat_log'

memory_cache = {
    CHAT_LOG: {}
}


def get_cache(key: str, sid: str):
    if sid not in memory_cache[key]:
        return []
    return memory_cache[key][sid]['data']


def save_cache(key: str, sid: str, data):
    cache_data = {
        'timestamp': get_timestamp(),
        'data': data
    }
    memory_cache[key][sid] = cache_data


def clean_expire_data():
    cur_timestamp = get_timestamp()
    for sid in list(memory_cache[CHAT_LOG].keys()):
        if memory_cache[CHAT_LOG][sid]['timestamp'] + CACHE_CHAT_LOG_EXPIRE < cur_timestamp:
            del memory_cache[CHAT_LOG][sid]


def clean():
    clean_expire_data()
    Timer(1, clean).start()


clean()
