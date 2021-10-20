# -*- coding: utf-8 -*-
import os
import re
from gensim.utils import deaccent
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# import string library function
import string

# Storing the sets of punctuation in variable result
puncts = list(string.punctuation)
# Storing stopwords
lang_stopwords = stopwords.words('english')
# Import wordNet lemmatizer
wordnet_lemmatizer = WordNetLemmatizer()


def text_preprocessor(text_corpus):
    """
    This function apply preprocessing steps for a given text corpus
    Parameters
    ----------
    text_corpus
        A list of original text
    Returns
    ------
        A list of clean text

    """
    clean_text = []
    for text in text_corpus:
        text = text.lower()
        text = remove_punctuation(text)
        text = remove_accent(text)
        text = remove_stopwords(text)
        text = apply_lemmatizer(text)
        clean_text.append(text)
    return clean_text


def remove_punctuation(text):
    """
    Remove punctuation for a given text

    Ps: Note that this is not be best way to achieve this task. it is only of demonstration purpose
    Parameters
    ----------
    text

    Returns
    -------

    """
    for punct in puncts:
        if punct in text:
            text = text.replace(punct, "")
    return text


def remove_accent(text):
    """
    Remove accent for a given text
    Parameters
    ----------
    text

    Returns
    -------

    """
    return deaccent(text)


def remove_stopwords(text):
    """
    Remove stopwords language for a given text

    Parameters
    ----------
    text

    Returns
    -------

    """
    return " ".join([t for t in text.split() if t not in lang_stopwords and t != ""])


def apply_lemmatizer(text):
    """
    Apply lemmatizer on the given text
    Parameters
    ----------
    text

    Returns
    -------

    """
    tokenization = nltk.word_tokenize(text)
    return " ".join([wordnet_lemmatizer.lemmatize(w) for w in tokenization])
