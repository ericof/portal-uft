"""Portal settings tests."""
from kitconcept import api
from portal_uft.testing import PORTAL_UFT_INTEGRATION_TESTING

import unittest


class TestPortalSettings(unittest.TestCase):
    """Testar se as configurações do portal estão corretas."""

    layer = PORTAL_UFT_INTEGRATION_TESTING

    def setUp(self) -> None:
        """Custom shared utility for tests"""
        super().setUp()
        self.portal = self.layer["portal"]

    def test_portal_title(self):
        """Testa se o título do portal está correto."""
        value = api.portal.get_registry_record("plone.site_title")
        expected = "Portal da UFT"
        self.assertEqual(value, expected)

    def test_portal_timezone(self):
        """Testa se o timezone está correto."""
        value = api.portal.get_registry_record("plone.portal_timezone")
        expected = "America/Araguaina"
        self.assertEqual(value, expected)

    def test_portal_sitemap(self):
        """Testa se o sitemap está habilitado."""
        value = api.portal.get_registry_record("plone.enable_sitemap")
        self.assertTrue(value)

    def test_portal_email_address(self):
        """Valida o endereço de email do portal."""
        value = api.portal.get_registry_record("plone.email_from_address")
        expected = "info@uft.edu.br"
        self.assertEqual(value, expected)

    def test_portal_email_name(self):
        """Valida o nome usado pelo email do portal."""
        value = api.portal.get_registry_record("plone.email_from_name")
        expected = "Portal da UFT"
        self.assertEqual(value, expected)
