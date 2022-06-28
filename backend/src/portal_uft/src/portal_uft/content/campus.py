"""A Campus in the site."""
from kitconcept import api
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from portal_uft.content.person import Person
from typing import List
from zope import schema
from zope.interface import implementer


class ICampus(Schema):
    """Schema of a campus."""

    city = schema.Choice(
        title=_("city", default="City"),
        vocabulary="portal_uft.vocabulary.cities",
        required=True,
    )


@implementer(ICampus)
class Campus(Container):
    """A campus in the site."""

    def persons(self) -> List[Person]:
        """Return a list of persons connected to this Campus."""
        persons = [
            rel.from_object
            for rel in api.relation.get(target=self, relationship="campus")
        ]
        return persons
