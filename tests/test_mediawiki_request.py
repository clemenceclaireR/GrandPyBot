#! /usr/bin/env python3
# coding: utf-8

import sys
import os
import requests_mock
# in order to not raise ValueError: attempted relative import beyond top-level package :
sys.path.append(os.path.realpath(''))
from app.api.media_wiki import WikiRequest
import requests


class TestMockWikiRequest:
    """
    Mock functions to be independant from the internet and test functions logic,
    doesn't fail if wikipedia page updated in between
    """

    def get_extract(self, url):
        """
        Personalised extract function for this test in order to not be dependant
        of the page_id function
        """
        wiki_data = requests.get(url)
        wiki_data = wiki_data.json()
        try:
            return wiki_data['query']['pages'][0]['extract']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def test_get_extract(self):
        """
        Get extract from wikipedia page, wikipedia page id is included
        """
        with requests_mock.Mocker() as mocker:
            page = 1187468
            result = '{"query": {"pages": [{"extract": ' \
                     '"Le Mont-Saint-Michel est une commune française située dans le département de la Manche ' \
                     'en Normandie. Elle tire son nom de l\'îlot rocheux consacré à saint Michel où ' \
                     's’élève aujourd’hui l’abbaye du Mont-Saint-Michel. L’architecture du Mont-Saint-Michel et ' \
                     'sa baie en font le site touristique le plus fréquenté de Normandie et l\'un des dix plus ' \
                     'fréquentés en France — premier site après ceux d\'Île-de-France — avec près de deux millions ' \
                     'et demi de visiteurs chaque année (3 250 000 en 2006, 2 300 000 en 2014)."}]}}'
            url_extract = WikiRequest.API_PAGEID_LINK.format(page)
            mocker.get(url_extract, text=result)
            assert self.get_extract(url_extract) == "Le Mont-Saint-Michel est une commune française située " \
                                                          "dans le département de la Manche en Normandie. Elle tire " \
                                                          "son nom de l'îlot rocheux consacré à saint Michel où s’élève " \
                                                          "aujourd’hui l’abbaye du Mont-Saint-Michel. L’architecture " \
                                                          "du Mont-Saint-Michel et sa baie en font le site touristique" \
                                                          " le plus fréquenté de Normandie et l'un des dix plus " \
                                                          "fréquentés en France — premier site après ceux " \
                                                          "d'Île-de-France — avec près de deux millions et " \
                                                          "demi de visiteurs chaque année (3 250 000 en 2006, " \
                                                          "2 300 000 en 2014)."

    def test_get_page_title(self):
        """
        Get wikipedia page title
        """
        with requests_mock.Mocker() as mocker:
            mt_st_michel = WikiRequest(48.636063, -1.511457)
            result = '{"query": {"geosearch": [{"title": "Le Mont-Saint-Michel"}]}}'
            mocker.get(mt_st_michel.url_page_id, text=result)
            assert mt_st_michel.get_page_title() == "Le Mont-Saint-Michel"

    def test_get_url(self):
        """
        Get wikipedia page url
        """
        with requests_mock.Mocker() as mocker:
            mt_st_michel = WikiRequest(48.636063, -1.511457)
            result = '{"query": {"pages": [{"fullurl": "https://fr.wikipedia.org/wiki/Le_Mont-Saint-Michel"}]}}'
            mocker.get('http://fr.wikipedia.org/w/api.php?action=query&prop=extracts|info&exsentences=3'
                                 '&inprop=url&explaintext=&titles={}&format=json&formatversion=2'
                       .format("Le Mont-Saint-Michel"), text=result)
            assert mt_st_michel.get_page_full_url("Le Mont-Saint-Michel") == "https://fr.wikipedia.org/wiki/Le_Mont-Saint-Michel"

    def test_get_page_id(self):
        """
        Get wikipedia page id
        """
        with requests_mock.Mocker() as mocker:
            mt_st_michel = WikiRequest(48.636063, -1.511457)
            result = '{"query": {"geosearch": [{"pageid": 1187468}]}}'
            mocker.get(mt_st_michel.url_page_id, text=result)
            assert mt_st_michel.get_page_id() == 1187468


class TestWikiRequest:
    """
    'Real' requests using Wikipedia API and real responses
    """
    def setup(self):
        self.mt_st_michel = WikiRequest(48.636063, -1.511457)

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
