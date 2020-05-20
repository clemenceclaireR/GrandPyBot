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

    #GET_SECTION_LINK = "https://fr.wikipedia.org/w/api.php?action=parse&pageid=5653202&format=json&section=1"

    def get_extract(self):
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
        wiki_data['query']['pages'][str(page_id)]['extract'] = json.dumps\
            (wiki_data['query']['pages'][str(page_id)]['extract'], ensure_ascii=False).encode('utf8')
        print("wiki data encoded >", wiki_data['query']['pages'][str(page_id)]['extract'])
        # decode
        wiki_data_decoded = wiki_data['query']['pages'][str(page_id)]['extract'].decode()
        print("wiki data decoded>", wiki_data_decoded)
        # enlever  Situation et accès et ce qu'il y a avant
        parsed_wikidata = wiki_data_decoded.split("accès", 1)[-1]
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
