from portal_uft.content.campus import Campus
from zope.lifecycleevent import ObjectAddedEvent


def _update_tags(obj: Campus):
    """Update tags on Campus object."""
    tags = set(obj.subject)
    city = obj.city
    tags.add(f"Campus: {city}")
    obj.subject = tuple(tags)


def added(obj: Campus, event: ObjectAddedEvent):
    """A new Campus was added to the site."""
    # Atualiza tags do objeto
    _update_tags(obj)
