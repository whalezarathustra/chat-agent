import hashlib
import random
import time

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()_+[]{};,./<>?'


def get_random_md5(num: int = 64):
    random.seed(time.time())
    r = random.choices(alphabet, k=num)
    m = hashlib.md5()
    m.update(''.join(r).encode(encoding='UTF-8'))
    return m.hexdigest()
