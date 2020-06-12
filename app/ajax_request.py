#! /usr/bin/env python3
# coding: utf-8

from flask import request, jsonify
from app.api.google_map import GoogleMapRequest
from app.api.media_wiki import WikiRequest
from app.parser.parser import Parser


def ajax_request():
    """
    Store user request, call the parser on it and get coordinates from
    GoogleMaps. Then call MediaWiki API to extract its description.
    """
    user_query = request.data.decode('utf-8')
    print("Requête =", user_query)

    parser = Parser()
    cleaned_query = parser.clean(user_query)
    print("Requête parsée =", cleaned_query)

    gmaps_request = GoogleMapRequest(cleaned_query)
    results = gmaps_request.extract_address_and_coordinates()
    print("Type de coords", results)
    status = results['status']
    print(status)
    if status != 'ZERO_RESULTS':
        coords = results['results'][0]['geometry']['location']
        print("Coordonnées GMaps =", results['results'][0]['geometry']['location'])
        address = results['results'][0]['formatted_address']
        print('addresse formatée', address, 'coordonnés', coords)

        if coords:
            wiki_request = WikiRequest(coords['lat'], coords['lng'])
            extract = wiki_request.get_extract()
            title = wiki_request.get_page_title()
            url = wiki_request.get_page_full_url(title)
            response = {'extract': extract, 'coords': coords, 'address': address, 'url': url}
            print("response >", response)

            return jsonify(response)
        else:
            response = ""
            return jsonify(response)

    else:
        response = ""
        return jsonify(response)
