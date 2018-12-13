from flask import Flask, jsonify, request
from dragnet import extract_content, extract_content_and_comments
from gensim.summarization.mz_entropy import mz_keywords
from gensim.summarization import keywords as textrank_keywords

app = Flask(__name__)


@app.route('/dragnet/content', methods=['POST'])
def dragnet_extract_content():
    return extract_content(request.data)


@app.route('/dragnet/content-comments', methods=['POST'])
def dragnet_extract_content_and_comments():
    return extract_content_and_comments(request.data)


@app.route('/gensim/mz-keywords', methods=['POST'])
def gensim_mz_keywords():
    return jsonify(mz_keywords(request.data))


@app.route('/gensim/textrank-keywords', methods=['POST'])
def gensim_textrank_keywords():
    return jsonify(textrank_keywords(request.data))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
