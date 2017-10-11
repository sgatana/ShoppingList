import unittest

from app.views import app


class Testingroutes(unittest.TestCase):
    def setUp(self):
        # create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_app_root(self):
        pass