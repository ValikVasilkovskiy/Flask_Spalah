import string
import random


def id_generator(size=10, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
