"""Test validators."""
from portal_uft import validators

import unittest


class TestEmailValidator(unittest.TestCase):
    """Test portal_uft.validators.is_valid_email."""

    def test_valid(self):
        values = [
            "bar@uft.edu.br",
            "foo@uft.edu.br",
        ]
        for value in values:
            self.assertTrue(validators.is_valid_email(value))

    def test_invalid(self):
        values = [
            "aa.palmas@uft.edu.br@mail.uft.edu.br",
            "foo@plone.org",
            "",
        ]
        for value in values:
            self.assertFalse(validators.is_valid_email(value))


class TestExtensionValidator(unittest.TestCase):
    """Test portal_uft.validators.is_valid_extension."""

    def test_valid(self):
        values = [
            "1234",
            "4521",
            "1977",
        ]
        for value in values:
            self.assertTrue(validators.is_valid_extension(value))

    def test_invalid(self):
        values = [
            "",
            "123",
            "123",
            "12345",
            "a1234",
            "foo@plone.org",
        ]
        for value in values:
            self.assertFalse(validators.is_valid_extension(value))
