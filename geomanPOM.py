import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pynput.mouse import Button, Controller
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from Locators import Locators
import json
import ast
import re
import time


class GeoManPOM():
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    def check_exists_by_xpath(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def get_circle_button(self):
        circle_list = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.circle_button_locator)))

        circle = circle_list[0]
        return circle

    def get_json_text_box(self):
        json_code = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.json_code_locator)))

        json_c = json_code[0]
        return json_c

    def draw_shape(self, shape):
        action = ActionChains(self.driver)
        json_c = self.get_json_text_box()
        action.move_to_element(json_c).click().perform()
        text = json_c.text
        while text != "1":
            action.move_to_element(json_c).send_keys(Keys.DELETE).perform()
            action.move_to_element(json_c).send_keys(Keys.BACKSPACE).perform()
            action.move_to_element(json_c).send_keys(Keys.UP).perform()
            text = json_c.text

        action.send_keys(shape).perform()

    def get_move_button(self):
        move_button_locator = "//*[@id='map']/div[2]/div[1]/div[3]/div[2]/a/div"
        move_button_list = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_all_elements_located((By.XPATH, move_button_locator)))
        move_button = move_button_list[0]

        return move_button

    def max_zoom(self):
        max_zoom_button_locator = "//*[@id='map']/div[2]/div[1]/div[1]/a[1]"
        max_zoom_button = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.max_zoom_button_locator)))
        max_zoom = max_zoom_button[0]

        return max_zoom

    def min_zoom(self):
        min_zoom_button = WebDriverWait(self.driver, 50).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.min_zoom_button_locator)))
        min_zoom = min_zoom_button[0]

        return min_zoom






