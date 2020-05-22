#! /usr/bin/env python3
# coding: utf-8


from flask import render_template, request, jsonify

from app import app
from app.forms import DialogForm
from app.api.google_map import GMAP_KEY, GoogleMapRequest
from app.api.media_wiki import WikiRequest
from app.parser.parser import Parser


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """
    Initiates the /index page (no other page in this app)
    """
    form = DialogForm()
    return render_template('index.html', form=form, key=GMAP_KEY)


@app.route('/ajax', methods=['POST'])
def ajax_request():
    """
    Store user request, call the parser on it and get coordinates from
    GoogleMaps. If coords corresponds to OC address, then call
    MediaWiki API to extract its description.
    """
    user_query = request.data.decode('utf-8')
    print("Requête =", user_query)

    parser = Parser()
    cleaned_query = parser.clean(user_query)
    print("Requête parsée =", cleaned_query)

    gmaps_request = GoogleMapRequest(cleaned_query)
    results = gmaps_request.extract_address_and_coordinates()
    print("Type de coords", results)
    coords = results['results'][0]['geometry']['location']
    print("Coordonnées GMaps =", results['results'][0]['geometry']['location'])
    address = results['results'][0]['formatted_address']
    print('addresse formatée', address, 'coordonnés', coords)

    if coords:
        if coords == {'lat': 48.8748465, 'lng': 2.3504873} : #  coords OC
            wiki_request = WikiRequest()
            extract = wiki_request.get_extract_OC()
            url = wiki_request.get_page_url()
            if extract:
                response = {'extract': extract, 'coords': coords, 'address': address, 'url': url}
            else:
                response = {'extract': "", 'coords': coords, 'address': address, 'url': url}
            print(">", extract, coords)
        else:
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
