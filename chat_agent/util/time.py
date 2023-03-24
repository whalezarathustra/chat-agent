import time


def get_timestamp():
    return int(time.time())


def get_timestamp_ms():
    return int(time.time() * 1000)
