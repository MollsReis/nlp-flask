# nlp-flask
### Common NLP functions on a Flask server (Dockerized)

Usage:
POST data to one of the following endpoints:
- `/dragnet/content` [Dragnet content extraction](https://github.com/dragnet-org/dragnet)
- `/dragnet/content-comments` [Dragnet content + comments extraction](https://github.com/dragnet-org/dragnet)
- `/gensim/textrank-keywords` [Keywords for TextRank summarization algorithm](https://radimrehurek.com/gensim/summarization/keywords.html)
- `/nlp/rake-keywords` [RAKE keyword extraction algorithm]()
- `/nlp/textrank-keywords` [Custom TextRank keyword extraction algorithm](https://en.wikipedia.org/wiki/PageRank)
