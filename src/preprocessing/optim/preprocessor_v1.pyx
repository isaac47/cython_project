# -*- coding: utf-8 -*-
import os
import re
from gensim.utils import deaccent
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# import string library function
import string

# Storing stopwords
lang_stopwords = stopwords.words('english')
# Import wordNet lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()


def text_preprocessor(list text_corpus):
    cdef:
        list clean_text = []
        list puncts = []
        str text
        int i, len_size

    # Storing the sets of punctuation in variable result
    puncts = list(string.punctuation)
    len_size = len(text_corpus)
    for i in range(len_size):
        text = text_corpus[i]
        text = text.lower()
        text = remove_punctuation(text, puncts)
        text = remove_accent(text)
        text = remove_stopwords(text)
        text = apply_lemmatizer(text)
        clean_text.append(text)
    return clean_text


cdef str remove_punctuation(str text, list puncts):
    cdef:
        str punct
        int j, len_size

    len_size = len(puncts)
    for j in range(len_size):
        punct = puncts[j]
        if punct in text:
            text = text.replace(punct, "")
    return text


cdef str remove_accent(str text):
    return deaccent(text)


cdef str remove_stopwords(str text):
    cdef:
        list tokens = []
        list result = []
        int j, len_size

    tokens = text.split()
    len_size = len(tokens)
    for j in range(len_size):
        tok = tokens[j]
        if tok not in lang_stopwords:
            result.append(tok)
    return " ".join(result)


cdef str apply_lemmatizer(str text):
    cdef:
        list tokenization = []
        list res = []
        int i, len_size

    tokenization = nltk.word_tokenize(text)
    len_size = len(tokenization)
    for i in range(len_size):
        tok = tokenization[i]
        res.append(wordnet_lemmatizer.lemmatize(tok))
    return " ".join(res)
