"""app/__init__.py application package constructor 
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
"""

from flask import Flask
from flask import rendender_template as f_render_template
from flask_bootstrap import Bootstrap 
from flask_mail import Mail 
from flask_moment import Moment 
from flask_sqlalchemy import SQLAlchemy 
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    # routes and custom error pages 

    return app