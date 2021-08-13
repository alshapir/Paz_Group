from pytest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Locators():
    text_aria_locator = "//*[@id='__layout']/div/main/div/div[2]/div[2]/div[1]/div/div/div/div[6]/div[1]/div"
    json_code_locator = "//*[@id='__layout']/div/main/div/div[2]/div[2]/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]"
    circle_button_locator = "//div[@id='map']/div[2]/div/div[2]/div[5]/a/div"
    Draw_Circle="""{"type": "FeatureCollection","features": [{"type": "FeatureCollection","features": [{"type": "Feature","properties": {"shape": "Circle","radius": 321.4449661096023,"name": "Unnamed Layer","category": "default"},"geometry": {"type": "Point","coordinates": [-74.006606, 40.713761]},"id": "e47b1c25-9d85-47e6-bf59-06672ade4bf7"}],"properties": {},"id": "4b7b0f9b-90a9-425e-8669-8ab947ca170b"}]}"""

    Draw_Poligon="""
        {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {
                "shape": "Polygon",
                "name": "Unnamed Layer",
                "category": "default"
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-74.00446, 40.719941],
                        [-74.008581, 40.718933],
                        [-74.008237, 40.71607],
                        [-74.005662, 40.713988],
                        [-73.999566, 40.714379],
                        [-73.998235, 40.718152],
                        [-74.00446, 40.719941]
                    ]
                ]
            },
            "id": "0a47a1d1-78a0-43f0-ab68-e19263dcd769"
        }]
    }"""
    Poligon_move_up = """
    {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "shape": "Polygon",
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-74.005447, 40.72495],
                    [-74.009568, 40.723942],
                    [-74.009224, 40.721079],
                    [-74.006649, 40.718997],
                    [-74.000553, 40.719388],
                    [-73.999222, 40.723161],
                    [-74.005447, 40.72495]
                ]
            ]
        },
        "id": "0a47a1d1-78a0-43f0-ab68-e19263dcd769"
    }]
}"""
    Poligon_move_left = """
    {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "shape": "Polygon",
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-73.990252, 40.724202],
                    [-73.994373, 40.723194],
                    [-73.994029, 40.720331],
                    [-73.991454, 40.718249],
                    [-73.985358, 40.71864],
                    [-73.984027, 40.722413],
                    [-73.990252, 40.724202]
                ]
            ]
        },
        "id": "0a47a1d1-78a0-43f0-ab68-e19263dcd769"
    }]
}"""

    Poligone_move_down = """
    {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "shape": "Polygon",
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-73.996733, 40.715908],
                    [-74.000854, 40.7149],
                    [-74.00051, 40.712037],
                    [-73.997935, 40.709955],
                    [-73.991839, 40.710346],
                    [-73.990508, 40.714119],
                    [-73.996733, 40.715908]
                ]
            ]
        },
        "id": "0a47a1d1-78a0-43f0-ab68-e19263dcd769"
    }]
}"""


    Draw_Poliline="""
    {
        "type": "FeatureCollection",
        "features": [{
            "type": "Feature",
            "properties": {
                "shape": "Line",
                "name": "Unnamed Layer",
                "category": "default"
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [-74.004975, 40.721827],
                    [-73.997205, 40.720461],
                    [-74.003429, 40.718217],
                    [-73.998064, 40.717046],
                    [-74.005662, 40.715029],
                    [-74.009611, 40.718737],
                    [-74.009353, 40.718867]
                ]
            },
            "id": "fa5aeb52-4114-4d2c-8068-ab12838e8664"
        }]
    }"""
    Edit_Poliline = """
    {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-74.004975, 40.721827],
                [-73.997205, 40.720461],
                [-74.003429, 40.718217]
            ]
        },
        "bbox": [-74.004975, 40.716136999999996, -73.997205, 40.723907000000004],
        "id": "22bdc7e2-dba5-4a49-ae30-1c2f5bc1eae5"
    }, {
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-74.003429, 40.718217],
                [-73.998064, 40.717046]
            ]
        },
        "bbox": [-74.003429, 40.717046, -73.998064, 40.718217],
        "id": "e0f1a9ed-27f2-4fcc-bde3-6afea0d337ce"
    }, {
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-73.998064, 40.717046],
                [-74.005662, 40.715029],
                [-74.009611, 40.718737],
                [-74.009353, 40.718867]
            ]
        },
        "bbox": [-74.009611, 40.715029, -73.998064, 40.718867],
        "id": "c64c9b12-f11e-426b-a780-ab817d071e41"
    }]
}"""

    Split_Poliline = """
    {
    "type": "FeatureCollection",
    "features": [{
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-74.004975, 40.721827],
                [-73.997205, 40.720461],
                [-74.003429, 40.718217]
            ]
        },
        "bbox": [-74.004975, 40.716136999999996, -73.997205, 40.723907000000004],
        "id": "22bdc7e2-dba5-4a49-ae30-1c2f5bc1eae5"
    }, {
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-74.003429, 40.718217],
                [-73.998064, 40.717046]
            ]
        },
        "bbox": [-74.003429, 40.717046, -73.998064, 40.718217],
        "id": "e0f1a9ed-27f2-4fcc-bde3-6afea0d337ce"
    }, {
        "type": "Feature",
        "properties": {
            "name": "Unnamed Layer",
            "category": "default"
        },
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-73.998064, 40.717046],
                [-74.005662, 40.715029],
                [-74.009611, 40.718737],
                [-74.009353, 40.718867]
            ]
        },
        "bbox": [-74.009611, 40.715029, -73.998064, 40.718867],
        "id": "c64c9b12-f11e-426b-a780-ab817d071e41"
    }]
}"""
    Drow_Empty_Screen = """
    {
        "type": "FeatureCollection",
        "features": []
    }"""

    max_zoom_button_locator="//*[@id='map']/div[2]/div[1]/div[1]/a[1]"
    min_zoom_button_locator="//*[@id='map']/div[2]/div[1]/div[1]/a[2]"

    def __init__(self):
        pass