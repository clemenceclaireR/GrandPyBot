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
        self.mt_st_michel = WikiRequest(48.636063, -1.511457)
        self.title = "Le Mont-Saint-Michel"

    def test_get_extract(self):
        assert self.mt_st_michel.get_extract() == "Le Mont-Saint-Michel est une commune française située dans " \
                                                  "le département de la Manche en Normandie. Elle tire son nom de " \
                                                  "l'îlot" \
                                                  " rocheux consacré à saint Michel où s’élève aujourd’hui l’abbaye du " \
                                                  "Mont-Saint-Michel.\nL’architecture du Mont-Saint-Michel et sa baie " \
                                                  "en font le site touristique le plus fréquenté de Normandie et l'un " \
                                                  "des dix plus fréquentés en France — premier site après ceux " \
                                                  "d'Île-de-France — avec près de deux millions et demi de " \
                                                  "visiteurs chaque année (3 250 000 en 2006, 2 300 000 en 2014)."

    def test_get_page_title(self):
        assert self.mt_st_michel.get_page_title() == "Le Mont-Saint-Michel"

    def test_get_url(self):
        assert self.mt_st_michel.get_page_full_url("Le Mont-Saint-Michel") == \
               "https://fr.wikipedia.org/wiki/Le_Mont-Saint-Michel"

    def test_get_page_id(self):
        assert self.mt_st_michel.get_page_id() == 1187468

