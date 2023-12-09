
# REQUIREMENTS 
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

# Database -- packages
import os 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

# Email -- packages
from flask_mail import Mail 
from threading import Thread 


# Database -- initialize 
basedir = os.path.abspath(os.path.dirname(__file__))




# app -- initialize
app = Flask(__name__) 



# CONFIG 
# forms -- configuration
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Database -- configuration 
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Email -- configuration
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')



# Templating -- initialise 
bootstrap = Bootstrap(app)

# Localization -- intialize 
moment = Moment(app)

# Database -- initialize 
db = SQLAlchemy(app) 
migrate = Migrate(app, db)

# Email -- initialize 
mail = Mail(app)



# MODELS 
# Database -- model definition 
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username



# EMAIL 

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr



# FORMS
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')



# Databases -- loading 

@app.shell_context_processor
def make_shell_sontext():
    return dict(db=db, User=User, Role=Role)


# ERRORS:  
# Templating -- error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# VIEWS: 
# Templating -- routes 
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))





