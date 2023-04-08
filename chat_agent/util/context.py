import threading


class ThreadLocalContextStorage:
    key_value = {}

    @classmethod
    def set(cls, data):
        cls.key_value.update({threading.current_thread(): data})

    @classmethod
    def get(cls):
        cur = threading.current_thread()
        if cur not in cls.key_value:
            cls.key_value[cur] = {}
        return cls.key_value[cur]

    @classmethod
    def clear_current_thread(cls):
        del cls.key_value[threading.current_thread()]

    @classmethod
    def clear_all_thread(cls):
        cls.key_value.clear()
        cls.key_value = {}


def get_thread_context():
    if not ThreadLocalContextStorage.get():
        ThreadLocalContextStorage.set({})
    return ThreadLocalContextStorage.get()


def get_thread_context_data(key: str):
    ctx = get_thread_context()
    return ctx.get(key)


def set_thread_context(ctx: dict = {}):
    ThreadLocalContextStorage.set(ctx)
