import networkx as nx
import numpy as np
import re
from nlp.stopwords import SEO_STOP_WORDS
# TODO from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize

NUM_RETURNED = 10
RADIUS = 4


def combine_keywords(keywords, doc):
    for word in keywords:
        others = keywords[:]
        others.remove(word)
        for other in others:
            if re.search(r'\b%s %s\b' % (word, other), doc):
                new_keywords = keywords[:]
                new_keywords.remove(word)
                new_keywords.remove(other)
                new_keywords = ['%s %s' % (word, other)] + new_keywords
                return combine_keywords(new_keywords, doc)
    return keywords


def textrank_keywords(doc, radius=RADIUS, num=NUM_RETURNED):
    # remove standalone digits and downcase doc
    clean_doc = re.sub(r'\b\d+\b', '', doc).lower()

    # tokenize doc and remove stopwords
    doc_tokens = list(w for w in word_tokenize(clean_doc) if w not in SEO_STOP_WORDS and w.isalpha())

    # get uniq vocab
    # TODO stemming
    vocab = list(set(doc_tokens))

    # create graph
    graph = nx.Graph()
    graph.add_nodes_from(vocab)
    for word in vocab:
        indices = list(idx for idx, val in enumerate(doc_tokens) if val == word)
        for idx in indices:
            neighbors = doc_tokens[max(0, idx - radius):min(len(doc_tokens) - 1, idx + radius + 1)]
            for n in neighbors:
                graph.add_edge(word, n)
    graph = nx.attr_matrix(graph, normalized=True, rc_order=vocab, dtype=np.float64)

    # do textrank (reduce graph to single vector)
    n = len(vocab)
    eps = 0.00001
    d = 0.85
    v = np.random.rand(n, 1)
    v = v / np.linalg.norm(v, 1)
    last_v = np.ones((n, 1), dtype=np.float64) * 100
    m_hat = (d * graph) + (((1 - d) / n) * np.ones((n, n), dtype=np.float64))
    while np.linalg.norm(v - last_v, 2) > eps:
        last_v = v
        v = np.matmul(m_hat, v)
    rankings = v

    # return top ranked phrases
    sorted_keywords = list(w[1] for w in sorted(enumerate(vocab), key=lambda x: -rankings[x[0]]))

    # combine adjacent keyword phrases
    print(sorted_keywords[0:num])
    return combine_keywords(sorted_keywords[0:num], ' '.join(doc_tokens))
