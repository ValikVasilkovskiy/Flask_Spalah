from flask import Flask, render_template, request, flash, redirect, url_for
from views import generate, generate_2, customers, RenderExample, customers_to_table
from SQLAlchemyEx import cust



app = Flask(__name__)
app.config.from_object('configs.DevConfig')


app.add_url_rule('/gen', view_func=generate)
app.add_url_rule('/gen2/<int:pass_len>', view_func=generate_2,)
app.add_url_rule('/customers', view_func=customers)
app.add_url_rule('/test-html',
                 view_func=RenderExample.as_view("render-example"),
)
app.add_url_rule('/customers_table', view_func=customers_to_table)
app.add_url_rule('/cust', view_func=cust)

if __name__ == '__main__':
    app.run()
