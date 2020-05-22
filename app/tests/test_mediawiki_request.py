#! /usr/bin/env python3
# coding: utf-8

import sys
import os
import requests_mock
# in order to not raise ValueError: attempted relative import beyond top-level package :
sys.path.append(os.path.realpath(''))
from app.api.media_wiki import WikiRequest


class TestWikiRequest:
    def setup(self):
        self.cite_paradis = WikiRequest()

    def test_get_extract(self):
        assert self.cite_paradis.get_extract_OC() == "La cité Paradis est une voie publique située dans le " \
                                                "10e arrondissement de Paris. Elle est en forme de té, une branche " \
                                                "débouche au 43, rue de Paradis, la deuxième au 57, " \
                                                  "rue d'Hauteville et la troisième en impasse."
