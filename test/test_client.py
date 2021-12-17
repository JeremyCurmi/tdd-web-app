import unittest
from src import client

class TestClient(unittest.TestCase):
    # { "ents": [], "html": "some string"}
    
    ## NerModelTestDouble('eng')
    def test_get_ents_returns_dictionary_given_empty_string(self):
        model = 'test'
        var = client.NamedEntityClient(model)
        ents = var.get_ents("")
        self.assertIsInstance(ents, dict)
        
    def test_get_ents_returns_list_given_nonempty_string(self):
        model = 'test'
        var = client.NamedEntityClient(model)
        ents = var.get_ents("This is a test")
        self.assertIsInstance(ents, list)