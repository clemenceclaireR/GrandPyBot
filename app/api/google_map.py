#! /usr/bin/env python3
# coding: utf-8

import requests
from os import environ

GMAP_KEY = environ.get('GMAPS_API_KEY')


class GoogleMapRequest:
    """
    handles request to Google Maps API
    """
    URL_BASE = "https://maps.googleapis.com/maps/api/geocode/json?address="

    def __init__(self, user_request):
        """
        Takes user input to merge it with the request to Google API
        """
        self.question = ".".join(user_request.split())
        self.url = GoogleMapRequest.URL_BASE + \
                   self.question + "&key=" + GMAP_KEY

    def get_data(self):
        """
        Get data from Google Map API and return it in a JSON format
        """
        gmaps_data = requests.get(self.url)
        api_data = gmaps_data.json()
        try:
            return api_data
        except IndexError or KeyError:
            return ""
