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
    coord = gmaps_request.get_coordinates()
    print("Coordonnées GMaps =", coord)

    if coord:
        if coord == {'lat': 48.8748465, 'lng': 2.3504873} : #  coord OC
            wiki_request = WikiRequest()
            extract = wiki_request.get_extract()
            if extract:
                response = {'extract': extract, 'coord': coord}
            else:
                response = {'extract': "", 'coord': coord}
            print(">", extract, coord)
        else:
            response = ""
        print("response >", response)

        return jsonify(response)
    else:
        response = {'extract': "", 'coord': coord}
        return jsonify(response)
