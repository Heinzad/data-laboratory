"""app/main/views.py : application routes in main blueprint
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
"""

from datetime import datetime
from flask import render_template as r_render_template
from . import main
from .forms import NameForm
from .. import db
from ..models import User 

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # ...
        return redirect(url_for('.index'))
    return r_render_template('index.html', 
                             form=form, 
                             name=session.get('name'), 
                             known=session.get('known', False),
                             current_datetime=datetime.utcnow()
                             )
