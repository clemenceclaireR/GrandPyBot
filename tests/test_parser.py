#! /usr/bin/env python3
# coding: utf-8

from app.parser.parser import Parser


class TestParser:
    def setup(self):
        self.parser = Parser()

    def test_get_to_lowercase(self):
        """
        Test the parser function to get request to lowercase
        """
        assert self.parser.clean(
            "OpenClassrooms"
        ) == "openclassrooms"

    def test_clean_stopwords(self):
        """
        Test the parser with the projects user request
        """
        assert self.parser.clean("Salut GrandPy ! Est-ce que tu connais l'adresse "
                                 "d'OpenClassrooms ?") == "d'openclassrooms"
