from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


CITIES = [
    ["palmas", "Palmas"],
    ["araguaina", "Araguaína"],
    ["gurupi", "Gurupi"],
    ["porto-nacional", "Porto Nacional"],
]


@provider(IVocabularyFactory)
def cities_vocabulary(context):
    """Vocabulary of cities in TO."""
    terms = []
    for token, title in CITIES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
