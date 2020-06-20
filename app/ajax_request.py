#! /usr/bin/env python3
# coding: utf-8

from flask import request, jsonify
from app.api.google_map import GoogleMapRequest
from app.api.media_wiki import WikiRequest
from app.parser.parser import Parser


def decode_request():
    return request.data.decode('utf-8')


def clean_user_query(user_query):
    parser = Parser()
    return parser.clean(user_query)


def check_if_status(results):
    status = results['status']
    if status != 'ZERO_RESULTS':
        return True


def ajax_request():
    """
    Store user request, call the parser on it and get coordinates from
    GoogleMaps. Then call MediaWiki API to extract its description.
    """
    user_query = decode_request()
    cleaned_query = clean_user_query(user_query)

    gmaps_request = GoogleMapRequest(cleaned_query)
    results = gmaps_request.extract_address_and_coordinates()

    if check_if_status(results):
        coords = results['results'][0]['geometry']['location']
        address = results['results'][0]['formatted_address']

        if coords:
            wiki_request = WikiRequest(coords['lat'], coords['lng'])
            extract = wiki_request.get_extract()
            title = wiki_request.get_page_title()
            url = wiki_request.get_page_full_url(title)
            response = {'extract': extract, 'coords': coords,
                        'address': address, 'url': url}
            return jsonify(response)
        else:
            response = ""
            return jsonify(response)

    else:
        response = ""
        return jsonify(response)
