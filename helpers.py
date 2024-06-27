import random
import string


def random_email():
    return 'myazova' + ''.join(random.choice(string.ascii_letters) for _ in range(10)) + "@yandex.ru"

def random_name():
    return ''.join(random.choice(string.ascii_letters) for _ in range(10))

def random_pass():
    return ''.join(random.choice(string.digits) for _ in range(10))