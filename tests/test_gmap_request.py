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
    requests mocking Google API response
    """

    def test_get_oc_address_coords(self):
        """
        Test a basic GoogleMapRequest with a mocked API
        response containing OC coordinates
        in order to run test without internet connection or overwrite
        """
        with requests_mock.Mocker() as mocker:
            oc_address = GoogleMapRequest("openclassrooms")
            result = '{"results" : [{"formatted_address": "7 Cité Paradis, ' \
                     '75010 Paris, France","geometry": {"location": ' \
                     '{"lat": 48.8748465, "lng": 2.3504873}}}]}'
            mocker.get(oc_address.url, text=result)
            results = oc_address.extract_address_and_coordinates()
            coords = results['results'][0]['geometry']['location']
            address = results['results'][0]['formatted_address']
            assert coords == {'lat': 48.8748465, 'lng': 2.3504873}
            assert address == '7 Cité Paradis, 75010 Paris, France'
"""
    #@pytest.mark.xfail(raises=IndexError)
    def test_fail_get_oc_address_coords(self):
        with requests_mock.Mocker() as mocker:
            oc_address = GoogleMapRequest("qws")
            result = '{"results" : [], "status": "ZERO_RESULTS"}'
            mocker.get(oc_address.url, text=result)
            results = oc_address.extract_address_and_coordinates()
                #raise  IndexError
            assert results == {'results': [], 'status': 'ZERO_RESULTS'}
            # 'status': 'ZERO_RESULTS'
"""
"""
class TestGMapsRequest:
    \"""
    'Real' requests using Google Maps API and real responses
    \"""

    def test_get_oc_address_coords(self):
        with requests_mock.Mocker() as mocker:
            oc_address = GoogleMapRequest("openclassrooms")
            mocker.get(oc_address.url, real_http=True)
            results = oc_address.extract_address_and_coordinates()
            coords = results['results'][0]['geometry']['location']
            address = results['results'][0]['formatted_address']
            assert coords == {'lat': 48.8748465, 'lng': 2.3504873}
            assert address == '7 Cité Paradis, 75010 Paris, France'


    def setup(self):
        self.openclassrooms = GoogleMapRequest("openclassrooms paris")

    def test_get_coord(self):
        results = self.openclassrooms.extract_address_and_coordinates()
        coords = results['results'][0]['geometry']['location']
        assert coords == {'lat': 48.8748465, 'lng': 2.3504873}

    def test_get_address(self):
        results = self.openclassrooms.extract_address_and_coordinates()
        address = results['results'][0]['formatted_address']
        assert address == '7 Cité Paradis, 75010 Paris, France'
    """
