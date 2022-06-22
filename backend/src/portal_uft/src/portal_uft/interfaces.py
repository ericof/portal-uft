"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPORTAL_UFTLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
