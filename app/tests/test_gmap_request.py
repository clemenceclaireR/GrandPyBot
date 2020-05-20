#! /usr/bin/env python
# coding: utf-8

import requests_mock
import os
import sys
# in order to not raise ValueError: attempted relative import beyond top-level package :
import json

sys.path.append(os.path.realpath(''))
from app.api.google_map import GoogleMapRequest


class TestMockGmap:

    def test_oc_address(self):
        """
        Test a basic GoogleMapRequest with a mocked API response containing OC coordinates
        in order to run test without internet connection or overwrite
        """
        with requests_mock.Mocker() as mocker:
            oc_address = GoogleMapRequest("J'ai trouvé leur adresse")
            result = '{"results" : [{"geometry": {"location": \
            {"lat": 48.875058, "lng": 2.350530}}}]}'
            mocker.get(oc_address.url, text=result)
            assert oc_address.get_coordinates() == {'lat': 48.875058, 'lng': 2.350530}


'''
        Differing items:
E         {'lng': 2.3504873} != {'lng': 2.35053}
E         {'lat': 48.8748465} != {'lat': 48.87505}

E         Differing items:
E         {'lat': 48.8749731} != {'lat': 48.875065}
E         {'lng': 2.3498414} != {'lng': 2.349852}

'''


class TestGMapsRequest:
    def setup(self):
        self.openclassrooms = GoogleMapRequest("openclassrooms paris")
        self.citeparadis = GoogleMapRequest("cité paradis")

    def test_get_coord(self):
        assert self.openclassrooms.get_coordinates() == {
            'lat': 48.8748465,
            'lng': 2.3504873
        }
        assert self.citeparadis.get_coordinates() == {
            'lat': 48.8749731,
            'lng': 2.3498414
        }


