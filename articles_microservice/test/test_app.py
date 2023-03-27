import unittest, sys

from flask import current_app

# from main import create_app
sys.path.append('..')
from app import create_app

class AppTestCase(unittest.TestCase):

    def test_setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    # def test_tearDown(self):
    #     self.app_context.pop()

    # test connection to db
    def test_app(self):
        self.assertIsNotNone(current_app)