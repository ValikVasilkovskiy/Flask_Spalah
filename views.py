from flask import request, Response, jsonify, render_template, redirect, url_for
from flask.views import MethodView
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, Table


from utils import id_generator, exec_query
from configs import SQL_ENGINE

class Customers(MethodView):
    def get(self):
        engine = SQL_ENGINE
        table_meta = MetaData(engine)
        customers_table = Table('customers', table_meta, autoload=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        results = session.query(customers_table)
        cols = [i['name'] for i in results.column_descriptions]

        res = [dict(zip(cols, i)) for i in results.all()]
        return render_template('customers.html', customers = res), session.close()

def generate():
    gen_len = int(request.args.get('len', 10))
    password = id_generator(size=gen_len)
    # response = Response(mimetype='application/xml')  # will fail in browser
    response = Response()
    response.data = password
    response.status_code = 201

    # manually parse QUERY_STRING to dict
    # 'http://127.0.0.1:5000/gen?len=12&abc=20'
    qs = request.environ['QUERY_STRING']
    qs_dict = {}
    for i in qs.split('&'):
        key, value = i.split('=')
        qs_dict[key] = value
    return response

def generate_2(pass_len):
    # '/gen2/<int:pass_len>'
    print(pass_len)
    print(type(pass_len))
    return id_generator(pass_len)

def cust():
    # /customers?state=null
    # /customers?state=IL
    # /customers

    state = request.args.get('state')
    query = 'SELECT * FROM customers'

    if state:
        if state.lower() == 'null':
            query += ' WHERE State IS NULL'
        else:
            query += ' WHERE State == "{st}"'.format(st=state.upper())

    res = exec_query(query + ';')
    res_dict = {
        item[0]: [value for value in item]
        for item in res
    }
    return jsonify(res_dict)


class RenderExample(MethodView):

    def get(self):
        context = {
            "users": ['Dima', 'Alex', "Sergey"],
            "form_data": request.args.get("firstname", "") + request.args.get("lastname", "")
        }

        return render_template(
            'render-example.html',
            context=context
        )

    def post(self):
        return render_template(
            'render-example.html',
            context={"request_data": str(request.form)}
        )



