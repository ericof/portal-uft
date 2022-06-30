from kitconcept import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from portal_uft import validators
from portal_uft.content.person import IPerson
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING
from zope.component import createObject

import unittest


class MockPerson:
    """Mock of a person."""


class PersonIntegrationTest(unittest.TestCase):

    layer = PORTAL_UFT_INTEGRATION_TESTING

    portal_type = "person"

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        fti = api.fti.get(self.portal_type)
        fti.global_allow = True

    def test_schema(self):
        fti = api.fti.get(self.portal_type)
        schema = fti.lookupSchema()
        self.assertEqual(IPerson, schema)

    def test_fti(self):
        fti = api.fti.get(self.portal_type)
        self.assertTrue(fti)

    def test_factory(self):
        fti = api.fti.get(self.portal_type)
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IPerson.providedBy(obj))

    def test_adding(self):
        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Alex Limi",
            description="Plone Founder",
            email="limi@uft.edu.br",
            extension="1999",
        )
        self.assertTrue(IPerson.providedBy(obj))
        self.assertEqual(obj, self.portal["alex-limi"])

    def test_invariant_validate_email_invalid(self):
        data = MockPerson()
        data.title = "Alex Limi"
        data.email = "limi@uft.edu.br"
        try:
            IPerson.validateInvariants(data)
        except validators.BadValue:
            pass

    def test_invariant_validate_email_valid(self):
        data = MockPerson()
        data.title = "Alex Limi"
        data.email = "alex.limi@uft.edu.br"
        IPerson.validateInvariants(data)

    def test_workflow_pending(self):
        # Criar person na raiz do site
        obj = api.content.create(
            container=self.portal,
            type=self.portal_type,
            title="Alex Limi",
            description="Plone Founder",
            email="limi@uft.edu.br",
            extension="1999",
        )
        # Fazer transição para o estado pending
        api.content.transition(obj, transition="submit")
        # Testar se Manager tem a permissão View
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.assertTrue(api.user.has_permission("View", obj=obj))
        # Testar se Anonymous tem a permissão View
        setRoles(self.portal, TEST_USER_ID, ["Anonymous"])
        self.assertTrue(api.user.has_permission("View", obj=obj))
