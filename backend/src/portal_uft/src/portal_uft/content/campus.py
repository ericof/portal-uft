"""A Campus in the site."""
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer


class ICampus(Schema):
    """Schema of a campus."""

    city = schema.TextLine(title=_("City"), required=True)


@implementer(ICampus)
class Campus(Container):
    """A campus in the site."""
