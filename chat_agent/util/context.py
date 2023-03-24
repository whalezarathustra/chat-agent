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


def set_thread_context(context: dict = {}):
    ThreadLocalContextStorage.set(context)


if __name__ == '__main__':
    set_thread_context(1)
    print(get_thread_context())
