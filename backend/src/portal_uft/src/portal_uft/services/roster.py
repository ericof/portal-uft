from collections import defaultdict
from kitconcept import api
from plone.restapi.services import Service


class RosterGet(Service):
    """Return a roster of Persons in a Campus."""

    def reply(self):
        """
        {
            "f": [{@id...}]
        }
        """
        campus = self.context
        persons = sorted(campus.persons(), key=lambda x: x.id)
        result = defaultdict(list)
        for person in persons:
            person_id = person.id
            result[person_id[0]].append(api.content.serialize(person, summary=True))
        return result
