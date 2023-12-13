"""app/main__init__.py main blueprint creation
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

