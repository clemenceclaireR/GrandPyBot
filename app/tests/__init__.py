#! /usr/bin/env python3
# coding: utf-8

import pytest
import requests_mock



def test_empty():
    """
    Test an empty GMapsRequest with a mocked API response
    """
    with requests_mock.Mocker() as m:
        empty = GMapsRequest("")
        m.get(empty.url, text="{}")
        assert empty.get_coordinates() == ""

