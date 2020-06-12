#! /usr/bin/env python3
# coding: utf-8


import json


class Parser:
    """
    Parses user request in order to keep useful words
    """
    def __init__(self):
        """
        Loads filter contained in the 'fr_stop_words_json' file
        """
        with open('app/parser/fr_stop_words.json', encoding='utf-8') as f:
            parsing_words = json.loads(f.read())
        self.stopwords = parsing_words["stopwords"]

    def clean(self, sentence):
        """
        get request to lowercase
        """
        sentence = sentence.lower()
        sentence = " ".join(
            w for w in sentence.split() if w not in self.stopwords)
        return sentence


if __name__ == "__main__":
    pass
