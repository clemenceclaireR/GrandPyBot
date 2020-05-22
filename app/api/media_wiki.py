#! /usr/bin/env python3
# coding: utf-8


import requests
import json


class WikiRequest:
    """
    Get the page from the Media Wiki API and get an extract
    """
    API_PAGEID_LINK = "https://fr.wikipedia.org/w/api.php?action=query&pageids={}" \
                      "&prop=extracts&explaintext=true&exsectionformat=plain&exsentences=3&format=json"
    API_GEOLOC_LINK = "https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&" \
                      "list=geosearch&gscoord={}|{}&gsradius=10000&gslimit=1&format=json"

    def __init__(self, *args):
        """Takes coordinates to build the url to request
        """
        try:
            self.latitude = args[0]
            self.longitude = args[1]
            self.url_page_id = WikiRequest.API_GEOLOC_LINK.format(self.latitude, self.longitude)
        except:
            pass

    def get_page_title(self):
        wiki_data = requests.get(self.url_page_id)
        wiki_data = wiki_data.json()
        try:
            title = wiki_data["query"]["geosearch"][0]["title"]
            return title
        except:
            return ""

    def get_page_full_url(self, title):
        wiki_data = requests.get('http://fr.wikipedia.org/w/api.php?action=query&prop=extracts|info&exsentences=3'
                                 '&inprop=url&explaintext=&titles={}&format=json&formatversion=2'.format(title))
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
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_extract(self):
        """
        Builds the url to request with the page id
        Returns an extract of the Wikipedia page
        """
        page_id = self.get_page_id()
        url_extract = WikiRequest.API_PAGEID_LINK.format(page_id)
        wiki_data = requests.get(url_extract)
        wiki_data = wiki_data.json()
        try:
            return wiki_data['query']['pages'][str(page_id)]['extract']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_extract_OC(self):
        """
        Builds the url to request with the page id
        Returns an extract of the Wikipedia page
        """
        page_id = '5653202'
        url_extract = WikiRequest.API_PAGEID_LINK.format(page_id)
        wiki_data = requests.get(url_extract)
        wiki_data = wiki_data.json()
        print("wiki response >", wiki_data['query']['pages'][str(page_id)]['extract'])
        # json to text in order to parse Situation et accès et ce qu'il y a avant
        wiki_data['query']['pages'][str(page_id)]['extract'] = json.dumps \
            (wiki_data['query']['pages'][str(page_id)]['extract'], ensure_ascii=False).encode('utf8')
        print("wiki data encoded >", wiki_data['query']['pages'][str(page_id)]['extract'])
        # decode
        wiki_data_decoded = wiki_data['query']['pages'][str(page_id)]['extract'].decode()
        print("wiki data decoded>", wiki_data_decoded)
        # enlever  Situation et accès et ce qu'il y a avant
        parsed_wikidata = wiki_data_decoded.split("accès\\n", 1)[-1]
        parsed_wikidata = parsed_wikidata.split("\"", 1)[0]
        # clean tous les "\n et "" "
        print("parsed response >", parsed_wikidata)
        # reconvertir en json
        wiki_data['query']['pages'][str(page_id)]['extract'] = parsed_wikidata
        print("back to json >", wiki_data)
        try:
            return wiki_data['query']['pages'][str(page_id)]['extract']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_page_url(self):
        url_str = 'https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis'
        return url_str
