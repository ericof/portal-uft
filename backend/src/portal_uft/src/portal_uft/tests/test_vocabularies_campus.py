from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


VOCABULARY = "portal_uft.vocabulary.campus"


class TestCampusVocabulary(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self) -> None:
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        # Create test content
        self.create_content()

    def create_content(self):
        contents = [
            # id, title, city
            ("palmas", "Palmas", "palmas"),
            ("araguaina", "Araguaína", "araguaina"),
        ]
        for id_, title, city in contents:
            api.content.create(
                container=self.portal,
                **{
                    "type": "campus",
                    "id": id_,
                    "title": title,
                    "description": f"Campus da UFT em {title}",
                    "city": city,
                    "email": f"{city}@uft.edu.br",
                },
            )

    def test_vocabulary(self):
        vocab = api.vocabulary.get(VOCABULARY)
        terms = [term for term in vocab]
        self.assertEqual(len(terms), 2)

    def test_vocabulary_titles(self):
        vocab = api.vocabulary.get(VOCABULARY)
        titles = [term.title for term in vocab]

        self.assertIn("Palmas", titles)
        self.assertIn("Araguaína", titles)
