""" app/posts/__init__.py 
--- Posts Blueprint and Template Rendering 
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

from flask import Blueprint

bp = Blueprint('posts', __name__)


# n.b. ordering prevents circular reference error 
from app.posts import routes
