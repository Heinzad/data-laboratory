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



# Database -- initialize 
basedir = os.path.abspath(os.path.dirname(__file__))


# app -- initialize
app = Flask(__name__) 
# forms -- configuration
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
# Database -- configuration 
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Templating -- initialise 
bootstrap = Bootstrap(app)

# Localization -- intialize 
moment = Moment(app)

# Database -- initialize 
db = SQLAlchemy(app) 
migrate = Migrate(app, db)




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
    

# Forms 
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')



# Databases -- loading 

@app.shell_context_processor
def make_shell_sontext():
    return dict(db=db, User=User, Role=Role)



# Templating -- error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 500

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



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
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False))





