"""A Person profile in the site."""
from plone.app.vocabularies.catalog import StaticCatalogVocabulary
from plone.dexterity.content import Container
from plone.supermodel.model import Schema
from portal_uft import _
from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class IPerson(Schema):
    """Schema of a person profile."""

    title = schema.TextLine(title=_("person_title", default="Fullname"), required=True)

    description = schema.Text(
        title=_("person_description", default="Biography"), required=False
    )

    campus = RelationList(
        title=_("person_campus", default="Campus"),
        required=False,
        default=[],
        value_type=RelationChoice(
            title=_("person_campus", default="Campus"),
            vocabulary=StaticCatalogVocabulary(
                {"portal_type": ["campus"], "review_state": "published"}
            ),
        ),
    )

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        pass


@implementer(IPerson)
class Person(Container):
    """A person profile in the site."""
