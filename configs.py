import os
from sqlalchemy import create_engine

base_dir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'chinook.db'
SQL_ENGINE = create_engine('sqlite:///{}\{}'.format(base_dir, DB_NAME), echo=False)


class Config:
    BASE_DIR = base_dir
    DEBUG = False
    SECRET_KEY = '< replace with a secret key > '
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True


class DevConfig(Config):
    DEBUG = True
    # DEBUG = False



