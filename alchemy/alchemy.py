"""alchemy.py : main script
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
""" 

import os 
from flask_migrate import Migrate
 

from app import create_app, db
from app.models import User, Role  



app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)

# Unit Test Launcher Command 
@app.cli.command()
def test():
    """Run unit tests""" 
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
 