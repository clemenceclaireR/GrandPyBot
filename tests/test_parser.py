#! /usr/bin/env python3
# coding: utf-8

import requests_mock
from app.parser.parser import Parser


class TestMockParser:
    def test_get_to_lowercase(self):
        with requests_mock.Mocker() as mocker:
            pass

    def test_clean_stopwords(self):
        with requests_mock.Mocker() as mocker:
            pass


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
