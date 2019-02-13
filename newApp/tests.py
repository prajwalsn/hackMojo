from app import app
import unittest 

#run using python -m unittest discover
"""
Basic Tests on the flask app
"""
class TestApp(unittest.TestCase): 

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def tearDown(self):
        pass 

    def test_get_movies_names(self):
        result = self.app.get('/get_movie_names') 
        self.assertEqual(result.status_code, 200) 

    def test_get_popup(self):
        result = self.app.get('/popup') 
        self.assertEqual(result.status_code, 200) 