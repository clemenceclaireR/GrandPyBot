#! /usr/bin/env python3
# coding: utf-8


import requests


class WikiRequest:
    """
    Get the page from the Media Wiki API and get an extract
    """
    API_PAGEID_LINK = "https://fr.wikipedia.org/w/api.php?action=query&pageids" \
                      "={}&prop=extracts&explaintext=true&exsectionformat=" \
                      "plain&exsentences=3&format=json"
    API_GEOLOC_LINK = "https://fr.wikipedia.org/w/api.php?action=query&prop=" \
                      "extracts&list=geosearch&gscoord={}|{}&gsradius=" \
                      "10000&gslimit=1&format=json"
    PAGE_ID = ""

    def __init__(self, *args):
        """
        Takes coordinates to build the url to request
        """
        try:
            self.latitude = args[0]
            self.longitude = args[1]
            self.url_page_id = WikiRequest.API_GEOLOC_LINK.\
                format(self.latitude, self.longitude)
        except:
            pass

    def get_page_title(self):
        """
        Get page title in order to use it to
        retrieve wiki url
        """
        wiki_data = requests.get(self.url_page_id)
        wiki_data = wiki_data.json()
        try:
            title = wiki_data["query"]["geosearch"][0]["title"]
            return title
        except:
            return ""

    def get_page_full_url(self, title):
        """
        Retrieve wikipedia url in order to give it with the extract
        """
        wiki_data = requests.get('http://fr.wikipedia.org/w/api.php?action='
                                 'query&prop=extracts|info&exsentences=3&'
                                 'inprop=url&explaintext=&titles={}&format'
                                 '=json&formatversion=2'.format(title))
        wiki_data = wiki_data.json()
        url = wiki_data["query"]["pages"][0]["fullurl"]

        return url

    def get_page_id(self):
        """
        Get wikipedia page id based on coordinates
        """
        wiki_data = requests.get(self.url_page_id)
        wiki_data = wiki_data.json()
        try:
            return wiki_data['query']['geosearch'][0]['pageid']
        except IndexError or KeyError:
            return ""

    def get_extract(self):
        """
        Builds the url to request with the page id
        Returns an extract of the Wikipedia page
        """
        WikiRequest.PAGE_ID = self.get_page_id()
        url_extract = WikiRequest.API_PAGEID_LINK.format(WikiRequest.PAGE_ID)
        wiki_data = requests.get(url_extract)
        wiki_data = wiki_data.json()
        try:
            return wiki_data['query']['pages'][str(WikiRequest.PAGE_ID)]['extract']
        except IndexError or KeyError:
            return ""
