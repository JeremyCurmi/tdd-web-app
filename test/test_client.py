import unittest
from src,client import NamedEntityClient


class TestClient(unittest.TestCase):
    # { "ents": [], "html": "some string"}

    ## NerModelTestDouble('eng')

    def setUp(self) -> None:
        self.model = 'test'
        self.client = NamedEntityClient(self.model)

    def test_get_ents_returns_dictionary_given_empty_string(self):
        ents = self.client.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string(self):
        ents = self.client.get_ents("This is a test")
        self.assertIsInstance(ents, list)
