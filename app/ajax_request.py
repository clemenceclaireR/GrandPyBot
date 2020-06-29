#! /usr/bin/env python3
# coding: utf-8

from flask import request, jsonify
from app.api.google_map import GoogleMapRequest
from app.api.media_wiki import WikiRequest
from app.parser.parser import Parser


def decode_request():
    """
    Returns decoded data in UTF-8
    """
    return request.data.decode('utf-8')


def clean_user_query(user_query):
    """
    Return parsed query
    """
    parser = Parser()
    return parser.clean(user_query)


def check_if_status(results):
    """
    Check if status is negative in order not to
    call for python scripts and returns empty response
    """
    status = results['status']
    if status != 'ZERO_RESULTS':
        return True


def ajax_request():
    """
    Store user request, call the parser on it and get coordinates from
    GoogleMaps. Then call MediaWiki API to extract its description.
    """
    # get query form form and parse it
    user_query = decode_request()
    cleaned_query = clean_user_query(user_query)

    # give the query to Google Maps API and store response
    gmaps_request = GoogleMapRequest(cleaned_query)
    results = gmaps_request.get_data()

    # if there is a status, store the coordinates and address
    if check_if_status(results):
        coords = results['results'][0]['geometry']['location']
        address = results['results'][0]['formatted_address']

        # if there is coordinates, give it to Wikipedia API
        # in order to extract needed information
        if coords:
            wiki_request = WikiRequest(coords['lat'], coords['lng'])
            extract = wiki_request.get_extract()
            title = wiki_request.get_page_title()
            url = wiki_request.get_page_full_url(title)
            response = {'extract': extract, 'coords': coords,
                        'address': address, 'url': url}
            # return response in Json format
            return jsonify(response)
        # if there is no coordinates, send an empty response
        else:
            response = ""
            return jsonify(response)
    # if there is no positive status, send an empty response
    else:
        response = ""
        return jsonify(response)
