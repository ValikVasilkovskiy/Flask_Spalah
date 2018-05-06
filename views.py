from flask import request, Response, jsonify
from utils import id_generator, exec_query

from pprint import pprint


def hello_world():
    return 'Hello, World!'


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
    print(qs_dict)

    # pprint(request.__dict__)
    pprint('=='*50)
    print(l('1231231231'))

    return response


def generate_2(pass_len):
    # '/gen2/<int:pass_len>'
    print(pass_len)
    print(type(pass_len))
    return id_generator(pass_len)


def customers():
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
    # response = Response(mimetype='application/json')
    # response.data = json.dumps(res_dict)
    # return response
    import json
    json_obj = json.dumps(res_dict)
    # json_obj = '{"1": null, "2": [1, 2], "3": -5.7}'
    python_dict = json.loads(json_obj)
    print(python_dict)
    print(type(python_dict))
    return jsonify(res_dict)











