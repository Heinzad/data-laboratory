""" app/main/routes.py 
--- Blueprint Routes 
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

from flask import render_template
from app.main import bp

@bp.route('/')
def index():
    return render_template('index.html')
