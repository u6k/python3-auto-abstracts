FROM python

RUN apt-get update && \
    apt-get install -y mecab libmecab-dev mecab-naist-jdic && \
    apt-get clean

RUN pip install mecab-python3 pyquery nltk numpy pycrypto six pdfminer.six

COPY japanese/ /opt/auto-abstracts/japanese/

ENTRYPOINT ["python", "/opt/auto-abstracts/japanese/auto_abstractor.py"]
