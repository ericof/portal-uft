"""A Person profile in the site."""
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel.model import Schema
from portal_uft import _
from zope import schema
from zope.interface import implementer


def is_valid_email(value: str) -> bool:
    """Check if email is from UFT."""
    return value.endswith("@uft.edu.br")


class IPerson(Schema):
    """Schema of a person profile."""

    title = schema.TextLine(title=_("person_title", default="Fullname"), required=True)

    description = schema.Text(
        title=_("person_description", default="Biography"), required=False
    )

    email = Email(
        title=_("person_email", default="E-mail"),
        required=True,
        constraint=is_valid_email,
    )

    extension = schema.TextLine(
        title=_(
            "Extension",
        ),
        required=False,
    )


@implementer(IPerson)
class Person(Container):
    """A person profile in the site."""
