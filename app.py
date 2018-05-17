from flask import Flask
from views import generate, generate_2, Customers, RenderExample

app = Flask(__name__)
app.config.from_object('configs.DevConfig')


app.add_url_rule('/gen', view_func=generate)
app.add_url_rule('/gen2/<int:pass_len>', view_func=generate_2,)

app.add_url_rule('/customers',
                 view_func=Customers.as_view('customers.html'),)
app.add_url_rule('/test-html',
                 view_func=RenderExample.as_view("render-example"),)


if __name__ == '__main__':
    app.run()
