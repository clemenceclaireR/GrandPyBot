#! /usr/bin/env python3
# coding: utf-8

import requests
import os

GMAP_KEY = os.environ.get('GMAPS_KEY', 'AIzaSyAcqisJEyTBEGTL_ExtFeYlbTWEcR7vDmA')


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
        self.url = GoogleMapRequest.URL_BASE + self.question + "&key=" + GMAP_KEY

    def get_coordinates(self):
        """
        Extracts coordinates (latitude, longitude) from
        the data returned by Google Maps API
        """
        api_data = self.get_data()
        try:
            #useful_result['coord'] = api_data['results'][0]['geometry']['location']
            #useful_result['address'] = api_data['result'][0]['formatted_address']
            return api_data
            #return api_data['results'][0]['geometry']['location'], api_data['result'][0]['formatted_address']
        except IndexError:
            return ""
        except KeyError:
            return ""

    def get_data(self):
        """
        Get data from Google Map API and return it in a JSON format
        """
        gmaps_data = requests.get(self.url)
        print("data >", gmaps_data.json())
        return gmaps_data.json()

    def get_formatted_address(self):
        """
        Extract formatted address from the data
        returned by Google Maps API
        """

        api_data = self.get_data()
        try:
            print(api_data['result'][0]['formatted_address'])
            return api_data['result'][0]['geometry']['location']
        except IndexError:
            return ""
        except KeyError:
            return ""

