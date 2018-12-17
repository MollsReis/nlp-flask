import re
from collections import defaultdict
from itertools import groupby
from nlp.stopwords import SEO_STOP_WORDS
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

NUM_RETURNED = 5
KEYWORD_PHRASE_MAX_LENGTH = 4
MINIMUM_FREQUENCY = 3


def rake_keywords(doc, num=NUM_RETURNED, max_length=KEYWORD_PHRASE_MAX_LENGTH, min_freq=MINIMUM_FREQUENCY):
    # remove standalone digits and downcase doc
    clean_doc = re.sub(r'\b\d+\b', '', doc).lower()

    # get a set of uniq phrases (split on stop words)
    groups = groupby([w for w in word_tokenize(clean_doc) if w.isalpha()], lambda w: w not in SEO_STOP_WORDS)
    phrases = list(tuple(g[1]) for g in groups if g[0])
    key_phrases = set(' '.join(p) for p in phrases if len(p) <= max_length)

    # get set of uniq words (stemmed)
    stemmer = PorterStemmer()
    uniq_words = set(stemmer.stem(w) for w in ' '.join(key_phrases).split())

    # bail out if there is no vocab
    if len(uniq_words) == 0:
        return []

    # calculate score of each word
    word_scores = defaultdict(lambda: 0)
    for word in uniq_words:
        freq = 0
        degree = 0
        for phrase in key_phrases:
            phrase_words = list(stemmer.stem(pw) for pw in phrase.split())
            if word in phrase_words:
                freq += 1
                degree += len(phrase_words)
        if freq >= min_freq:
            word_scores[word] = degree / float(freq)

    # calculate aggregate scores for each phrase
    phrase_scores = dict()
    for phrase in key_phrases:
        score = 0
        for word in phrase.split():
            score += word_scores[stemmer.stem(word)]
        phrase_scores[phrase] = score

    # return top $num phrases by score
    ranked_phrases = sorted(list(phrase_scores.keys()), key=lambda k: -phrase_scores[k])
    return ranked_phrases[0:num]
