"""Validators."""
from portal_uft import _
from zope.interface import Invalid

import re


class BadValue(Invalid):
    """Exception raised when a provided value is informed."""

    __doc__ = _("The value is not correct")


def is_valid_email(value: str) -> bool:
    """Check if email is from UFT."""
    return value.endswith("@uft.edu.br")


def is_valid_extension(value: str) -> bool:
    """Check if extension is valid."""
    return re.match(r"^\d{4}$", value)


def is_valid_username(title: str, email: str) -> bool:
    """Check if username matches our pattern."""
    username = email.split("@")[0]
    expected = title.lower().replace(" ", ".")
    return username == expected
