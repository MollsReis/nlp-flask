# nlp-flask
### Common NLP functions on a Flask server (Dockerized)

Usage:
POST data to one of the following endpoints:
- `/dragnet/content` [Dragnet content extraction](https://github.com/dragnet-org/dragnet)
- `/dragnet/content-comments` [Dragnet content + comments extraction](https://github.com/dragnet-org/dragnet)
- `/gensim/mz-keywords` [Keywords for the Montemurro and Zanette entropy algorithm](https://radimrehurek.com/gensim/summarization/mz_entropy.html)
- `/gensim/textrank-keywords` [Keywords for TextRank summarization algorithm](https://radimrehurek.com/gensim/summarization/keywords.html)
