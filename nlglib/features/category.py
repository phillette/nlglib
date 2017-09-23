# encoding: utf-8

"""Definition of the lexical categories."""

from __future__ import unicode_literals

#  A default value, indicating an unspecified category.
ANY = "ANY"

#  The element represents a symbol.
SYMBOL = "SYMBOL"

#  A noun element.
NOUN = "NOUN"

#  An adjective element.
ADJECTIVE = "ADJECTIVE"

#  An adverb element.
ADVERB = "ADVERB"

#  A verb element.
VERB = "VERB"

#  A determiner element often referred to as a specifier.
DETERMINER = "DETERMINER"

# A numeral denotes a number (eg one, but also first)
NUMERAL = 'NUMERAL'

#  A pronoun element.
PRONOUN = "PRONOUN"

#  A conjunction element.
CONJUNCTION = "CONJUNCTION"

#  A preposition element.
PREPOSITION = "PREPOSITION"

# Eg 'to' or 'up' in 'look up'
PARTICLE = 'PARTICLE'

# A word or expression that occurs as an utterance
# on its own and expresses a spontaneous feeling or reaction.
# Ouch! Damn! ...
INTERJECTION = 'INTERJECTION'

#  A complementiser element.
COMPLEMENTISER = "COMPLEMENTISER"

#  A modal element.
MODAL = "MODAL"

#  An auxiliary verb element.
AUXILIARY = "AUXILIARY"

CLAUSE = "CLAUSE"
ADJECTIVE_PHRASE = "ADJECTIVE_PHRASE"
ADVERB_PHRASE = "ADVERB_PHRASE"
NOUN_PHRASE = "NOUN_PHRASE"
PREPOSITION_PHRASE = "PREPOSITION_PHRASE"
VERB_PHRASE = "VERB_PHRASE"
CANNED_TEXT = "CANNED_TEXT"

# Full document
DOCUMENT = "DOCUMENT"
# RST relation
RST = "RST"
# Message Specification
MSG = 'MSG'

TAGS = [
    ANY,
    ADJECTIVE,
    ADVERB,
    AUXILIARY,
    COMPLEMENTISER,
    CONJUNCTION,
    DETERMINER,
    INTERJECTION,
    MODAL,
    NOUN,
    NUMERAL,
    PARTICLE,
    PREPOSITION,
    PRONOUN,
    SYMBOL,
    VERB,
]