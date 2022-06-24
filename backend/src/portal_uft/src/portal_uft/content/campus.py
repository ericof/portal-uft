"""A Person profile in the site."""
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class ICampus(Schema):
    """Schema of a campus."""


@implementer(ICampus)
class Campus(Container):
    """A campus in the site."""
