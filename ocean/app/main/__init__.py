""" app/main/__init__.py 
--- Main Blueprint & Template Rendering
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

from flask import Blueprint


bp = Blueprint('main', __name__)

from app.main import routes

