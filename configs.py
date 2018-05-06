import os

base_dir = os.path.abspath(os.path.dirname(__file__))

__builtins__["l"] = len

class Config:
    BASE_DIR = base_dir
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    # DEBUG = False
