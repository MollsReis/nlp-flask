FROM python:3
WORKDIR src
RUN pip install --upgrade pip
RUN pip install lxml numpy Cython
RUN pip install dragnet gensim nltk networkx flask
RUN python -m nltk.downloader punkt
COPY server.py server.py
COPY nlp nlp
EXPOSE 5000
ENTRYPOINT ["python", "server.py"]
