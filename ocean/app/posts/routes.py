""" app/posts/routes.py 
--- Posts Routes 
--- ------------- --- 
--- 20231214 initial commit from Abdelhadi Dyouri (2022) 
-- "How To Structure a Large Flask Application" 
--- ------------- --- 
"""

from flask import render_template

from app.posts import bp
from app.extensions import db
from app.models.post import Post 


@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)

@bp.route('/categories/')
def categories():
    return render_template('posts/categories.html')

