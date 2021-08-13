from ChooseDriver import GetWebDriver

class NavigateTo():
    driver = ''
    def __init__(self):
        pass

    def NavigateToUrl(self, url, browser):
        choose = GetWebDriver()
        self.driver = choose.ReturnWebDriver(browser)
        self.driver.get(url)

        return self.driver
