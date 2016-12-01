import os
import sys
import unittest
import tempfile
sys.path.insert(0, os.path.abspath('..'))
import bauble

class BaubleTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = bauble.app.test_client()

    def tearDown(self):
        pass

    def test_default_page_returns_200(self):
        rv = self.app.get('/')
        assert '200' in rv.status

    def test_generator_page_returns_200(self):
        rv = self.app.get('/generator/1')
        assert '200' in rv.status

    def test_generator_page_only_takes_int_not_str(self):
        rv = self.app.get('/generator/hello')
        assert '404' in rv.status


if __name__ == '__main__':
    unittest.main()

