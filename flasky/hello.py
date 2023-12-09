# app - packages
from flask import Flask 

# Templating -- packages
from flask import render_template
from flask_bootstrap import Bootstrap

# Localization -- packages
from flask_moment import Moment 
from datetime import datetime 

# Forms -- packages
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField 
from wtforms.validators import DataRequired 

# redirects & user sessions -- packages
from flask import session, redirect, url_for 

import os 



# app -- initialize
app = Flask(__name__) 
# forms -- configuration
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Templating -- initialise 
bootstrap = Bootstrap(app)

# Localization -- intialize 
moment = Moment(app)



# Templating -- routes 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


# Templating -- error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Forms 
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
