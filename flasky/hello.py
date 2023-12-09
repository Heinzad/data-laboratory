# app - packages
from flask import Flask 

# Templating -- packages
from flask import render_template
from flask_bootstrap import Bootstrap

# Localization -- packages
from flask_moment import Moment 
from datetime import datetime 



# app -- initialize
app = Flask(__name__)

# Templating -- initialise 
bootstrap = Bootstrap(app)

# Localization -- intialize 
moment = Moment(app)


# Templating -- routes
@app.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow()
                           )

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# Templating -- error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
