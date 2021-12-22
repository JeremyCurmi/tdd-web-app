import unittest
import json
from flask import request
from src.app.app import app


class TestApi(unittest.TestCase):

    def test_ner_endpoint_given_json_body_returns_200(self):
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Steve Malkmus is a good band."})
            assert response._status_code == 200
    """ we can include more unit tests here"""

    def test_ner_endpoint_given_json_boyd_with_known_entities_returns_entity_result_in_response(self):
        """integration test"""
        with app.test_client() as client:
            response = client.post('/ner', json={"sentence": "Kamala Harris"})
            data = json.loads(response.get_data())
            self.assertTrue(len(data["entities"]) > 0)
            self.assertTrue(data["entities"][0]["label"] == "Person")
