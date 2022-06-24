from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft.content.campus import ICampus
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING
from zope.component import createObject

import unittest


class CampusIntegrationTest(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    portal_type = "campus"

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = api.fti.get(self.portal_type)
        fti.global_allow = True

    def test_schema(self):
        fti = api.fti.get(self.portal_type)
        schema = fti.lookupSchema()
        self.assertEqual(ICampus, schema)

    def test_fti(self):
        fti = api.fti.get(self.portal_type)
        self.assertTrue(fti)

    def test_factory(self):
        fti = api.fti.get(self.portal_type)
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ICampus.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Palmas",
            description="Campus da UFT em Palmas",
            city="palmas",
            email="palmas@uft.edu.br",
            extension="2022",
        )
        self.assertTrue(ICampus.providedBy(obj))
        self.assertEqual(obj, self.portal["palmas"])

    def test_subscriber_added(self):
        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Palmas",
            description="Campus da UFT em Palmas",
            city="palmas",
            email="palmas@uft.edu.br",
            extension="2022",
        )
        self.assertIn("Campus: Palmas", obj.subject)

    def test_subscriber_modified(self):
        from zope.event import notify
        from zope.lifecycleevent import ObjectModifiedEvent

        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Palmas",
            description="Campus da UFT em Palmas",
            email="palmas@uft.edu.br",
            city="palmas",
            extension="2022",
        )
        obj.city = "araguaina"
        notify(ObjectModifiedEvent(obj))
        self.assertIn("Campus: Araguaína", obj.subject)
