import re
from nlp.stopwords import SEO_STOP_WORDS

DEFAULT_NUM_RETURNED = 5
KEYWORD_PHRASE_MAX_LENGTH = 4
MINIMUM_FREQUENCY = 3

STOP_WORD_REGEX = re.compile('|'.join('(?<=\\s)%s(?=\\s)' % w for w in SEO_STOP_WORDS), re.IGNORECASE)


def rake_keywords(doc, num = DEFAULT_NUM_RETURNED):
    # get a set of uniq phrases (split on stop words)
    phrase_iter = re.finditer(STOP_WORD_REGEX, doc)
    phrases = {p for p in phrase_iter if len(str(p).split(' ')) < KEYWORD_PHRASE_MAX_LENGTH}
    return phrases

    # TODO get set of uniq words (stemmed)
    # TODO calculate score of each word
    # TODO calculate aggregate scores for each phrase
    # TODO return top $num phrases by score
    pass
