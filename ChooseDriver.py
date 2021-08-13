import os
from selenium.webdriver import Chrome
from selenium import webdriver


class GetWebDriver():
    driver = ''
    currentlocation = ""
    def __init__(self):
        pass

    def find_location(self):
        self.currentlocation = os.path.dirname(os.path.abspath("chromedriver.exe"))

    def ReturnWebDriver(self, browsername):
        self.find_location()
        fullpath = self.currentlocation + "\\chromedriver.exe"
        if str(browsername).lower() == "chrome":
            self.driver = webdriver.Chrome(fullpath)
            self.driver.maximize_window()
            self.driver.implicitly_wait(50)

        return self.driver