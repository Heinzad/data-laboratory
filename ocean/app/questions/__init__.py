""" app/questions/__init__.py 
--- Questions & Answers Blueprint 
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

from flask import Blueprint

bp = Blueprint('questions', __name__)


# n.b. ordering prevents circular reference error 
from app.questions import routes
