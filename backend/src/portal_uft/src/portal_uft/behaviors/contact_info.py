from plone.autoform.interfaces import IFormFieldProvider
from plone.schema.email import Email
from plone.supermodel import model
from portal_uft import _
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IContactInfo(model.Schema):
    """Contact Information behavior."""

    model.fieldset("contact", label=_("Contact"), fields=["email", "extension"])
    email = Email(title=_("person_email", default="E-mail"), required=True)

    extension = schema.TextLine(
        title=_(
            "Extension",
        ),
        required=False,
    )
