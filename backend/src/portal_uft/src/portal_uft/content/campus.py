"""A Campus in the site."""
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from zope.interface import implementer


class ICampus(Schema):
    """Schema of a campus."""


@implementer(ICampus)
class Campus(Container):
    """A campus in the site."""
