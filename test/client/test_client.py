import unittest
from src.client.client import NamedEntityClient
from .test_doubles import NerModelTestDouble


class TestClient(unittest.TestCase):

    def setUp(self) -> None:
        self.model = NerModelTestDouble('eng')

    def test_get_ents_returns_dictionary_given_empty_string_causes_empty_spacy_doc_ents(self):
        self.model.returns_doc_ents([])
        ner = NamedEntityClient(self.model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dictionary_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        self.model.returns_doc_ents([])
        ner = NamedEntityClient(self.model)
        ents = ner.get_ents("Madison is a city in Malta")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        doc_ents = [{"text": "Jeris Rumi","label_":"PERSON"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "Jeris Rumi","label":"Person"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        doc_ents = [{"text": "Lithuanian","label_":"NORP"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "Lithuanian","label":"Group"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        doc_ents = [{"text": "The ocean", "label_": "LOC"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "The ocean", "label": "Location"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        doc_ents = [{"text": "ASL", "label_": "LANGUAGE"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "ASL", "label": "Language"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        doc_ents = [{"text": "Australia", "label_": "GPE"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "Australia", "label": "Location"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        doc_ents = [{"text": "Australia", "label_": "GPE"}, {"text":"Judith Polgar","label_":"PERSON"}]
        self.model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(self.model)
        result = ner.get_ents("...")
        expected = {"ents": [{"ent": "Australia", "label": "Location"}, {"ent": "Judith Polgar", "label": "Person"}], "html": ""}
        self.assertListEqual(result["ents"], expected["ents"])