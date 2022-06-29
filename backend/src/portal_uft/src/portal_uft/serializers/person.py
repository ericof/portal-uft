from kitconcept import api
from plone.restapi.interfaces import ISerializeToJson
from plone.restapi.serializer.dxcontent import SerializeToJson
from portal_uft.content.person import IPerson
from portal_uft.interfaces import IPORTAL_UFTLayer
from zope.component import adapter
from zope.interface import implementer


@implementer(ISerializeToJson)
@adapter(IPerson, IPORTAL_UFTLayer)
class PersonSerializer(SerializeToJson):
    """Serialize a Person object to JSON."""

    def __call__(self, **kwargs):
        serialization = super().__call__(**kwargs)
        campus = serialization["campus"]
        for item in campus:
            token = item.get("token")
            obj = api.content.get(UID=token)
            item["@id"] = f"{obj.absolute_url()}"
        return serialization
