#! /usr/bin/env python
# coding: utf-8

import requests_mock
import os
import sys
import pytest
# in order to not raise ValueError: attempted relative
# import beyond top-level package :
sys.path.append(os.path.realpath(''))
from app.api.google_map import GoogleMapRequest


class TestMockGmap:
    """
    Mock request for Google API response
    """

    def test_get_oc_address_coords(self):
        """
        Mock request to get a response containing OC coordinates
        in order to run test without internet connection or overwrite
        """
        with requests_mock.Mocker() as mocker:
            oc_address = GoogleMapRequest("openclassrooms")
            result = '{"results" : [{"formatted_address": "7 Cité Paradis, ' \
                     '75010 Paris, France","geometry": {"location": ' \
                     '{"lat": 48.8748465, "lng": 2.3504873}}}]}'
            mocker.get(oc_address.url, text=result)
            results = oc_address.get_data()
            coords = results['results'][0]['geometry']['location']
            address = results['results'][0]['formatted_address']
            assert coords == {'lat': 48.8748465, 'lng': 2.3504873}
            assert address == '7 Cité Paradis, 75010 Paris, France'


class TestGMapsRequest:
    """
    'Real' requests using Google Maps API and real responses
    """

    def setup(self):
        self.openclassrooms = GoogleMapRequest("openclassrooms paris")

    def test_get_address_and_coord(self):
        """
        Call get_data() function to extract needed informations
        """
        results = self.openclassrooms.get_data()
        coords = results['results'][0]['geometry']['location']
        address = results['results'][0]['formatted_address']
        assert coords == {'lat': 48.8748465, 'lng': 2.3504873}
        assert address == '7 Cité Paradis, 75010 Paris, France'



