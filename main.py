from flask import Flask, request
from utils import id_generator
app = Flask(__name__)


@app.route('/index')
def hello_world():
    return 'Hello, World!'


@app.route('/gen')
def generate():
    gen_len = int(request.args.get('len', 10))
    return id_generator(size=gen_len)


app.run(debug=True)
