from flask import jsonify, render_template
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table
import os


base_dir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = 'chinook.db'

def cust():
    engine = create_engine('sqlite:///{}\{}'.format(base_dir, DB_NAME), echo=False)
    tablemeta = MetaData(engine)
    table = Table('customers', tablemeta, autoload=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(table)
    cols = [i['name'] for i in results.column_descriptions]

    res = [dict(zip(cols, i)) for i in results.all()]

    return render_template('cust.html', customers = res), session.close()

