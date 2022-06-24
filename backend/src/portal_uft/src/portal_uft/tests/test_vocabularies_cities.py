from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


VOCABULARY = "portal_uft.vocabulary.cities"


class TestCitiesVocabulary(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self) -> None:
        self.portal = self.layer["portal"]

    def test_vocabulary(self):
        vocab = api.vocabulary.get(VOCABULARY)
        terms = [term for term in vocab]
        self.assertEqual(len(terms), 4)

    def test_vocabulary_titles(self):
        vocab = api.vocabulary.get(VOCABULARY)
        titles = [term.title for term in vocab]

        self.assertIn("Palmas", titles)
        self.assertIn("Araguaína", titles)
        self.assertIn("Gurupi", titles)
