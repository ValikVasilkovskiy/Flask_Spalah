from flask import Flask
from views import hello_world, generate, generate_2, customers, RenderExample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config.from_object('configs.DevConfig')

app.add_url_rule('/index', view_func=hello_world)
app.add_url_rule('/gen', view_func=generate)
app.add_url_rule('/gen2/<int:pass_len>', view_func=generate_2,)
app.add_url_rule('/customers', view_func=customers)
app.add_url_rule('/test-html',
                 view_func=RenderExample.as_view("render-example"),
)

# toolbar = DebugToolbarExtension(app)
# app.config['SECRET_KEY'] = '<replace with a secret key>'
# app.config['DEBUG_TB_ENABLED'] = True

app.run()
