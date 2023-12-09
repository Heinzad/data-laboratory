"""tests/test_basics.py : unit tests
-- reference: Miguel Grinberg (2018). Flask Web Development: Developing Web Applications with Python. O'Reilly. 

-- 20231209 initial commit: Adam Heinz 
"""

import unittest as ut

from flask import current_app as f_current_app
from app import create_app, db

class BasicsTestCase(ut.TestCase()):
    
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app.context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(f_current_app is None)
    
    def test_app_is_testing(self):
        self.assertTrue(f_current_app.config['TESTING'])
