import os
import string
import random
import sqlite3

from configs import Config

DB_NAME = 'chinook.db'
DB_PATH = os.path.join(Config.BASE_DIR, DB_NAME)


def exec_query(query):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    res = [row for row in c.execute(query)]
    conn.close()
    return res


def id_generator(size=10, chars=string.ascii_letters):
    return ''.join(random.choice(chars) for _ in range(size))
