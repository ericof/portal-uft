"""A Person profile in the site."""
from plone.dexterity.content import Container
from plone.schema.email import Email
from plone.supermodel.model import Schema
from portal_uft import _
from portal_uft import validators
from zope import schema
from zope.interface import implementer
from zope.interface import invariant


class IPerson(Schema):
    """Schema of a person profile."""

    title = schema.TextLine(title=_("person_title", default="Fullname"), required=True)

    description = schema.Text(
        title=_("person_description", default="Biography"), required=False
    )

    email = Email(
        title=_("person_email", default="E-mail"),
        required=True,
    )

    extension = schema.TextLine(
        title=_(
            "Extension",
        ),
        required=False,
        constraint=validators.is_valid_extension,
    )

    @invariant
    def validate_email(data):
        """Validate email set by the user."""
        value = data.email
        if not (value and validators.is_valid_email(value)):
            raise validators.BadValue(
                f"The email {value} is not in the uft.edu.br domain."
            )


@implementer(IPerson)
class Person(Container):
    """A person profile in the site."""
