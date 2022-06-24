from kitconcept import api
from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent
from zope.lifecycleevent import ObjectModifiedEvent


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    vocab = api.vocabulary.get("portal_uft.vocabulary.cities")
    tags = {tag for tag in obj.subject if not tag.startswith("Campus: ")}
    city = obj.city
    term = vocab.getTermByToken(city)
    tags.add(f"Campus: {term.title}")
    obj.subject = tuple(tags)


def added(obj: Campus, event: ObjectAddedEvent):
    """A new Campus was added to the site."""
    # Atualiza tags do objeto
    _update_tags(obj)


def modified(obj: Campus, event: ObjectModifiedEvent):
    """A Campus object was modified."""
    # Atualiza tags do objeto
    _update_tags(obj)
