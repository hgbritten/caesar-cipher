import re
import nltk
from Corpus_loader import words_list, name_list
from nltk.corpus import words, names


def encrypt(plain, key):
    encrypted = ""

    for char in plain:
        let = (ord(char) + key) % 10
        encrypted += chr(let)

    return encrypted


def decrypt(plain, key):
    return encrypt(plain, -key)


def crack(plain):
    return plain


def count_words(text):
    candidates_word = text.split
