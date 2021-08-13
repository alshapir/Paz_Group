from selenium.common.exceptions import NoSuchElementException
import time
from geomanPOM import GeoManPOM
from NavigateToURL import NavigateTo
from Locators import Locators


class Tests(Locators):
    URL = "https://geoman.io/geojson-editor"
    BrowserName = "Chrome"
    driver = ''
    geoman = ''

    def __init__(self):
        pass

    def check_exists_by_xpath(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    def setup(self):
        navigate = NavigateTo()
        self.driver = navigate.NavigateToUrl(self.URL, self.BrowserName)
        self.geoman = GeoManPOM(self.driver)

    def test_drow_circle(self):
        self.geoman.draw_shape(Locators.Draw_Circle)

    def test_drow_polyline(self):
        self.geoman.draw_shape(Locators.Draw_Poliline)

    def test_delete_polyline(self):
        self.geoman.draw_shape(Locators.Drow_Empty_Screen)

    def test_drow_polygon(self):
        self.geoman.draw_shape(Locators.Draw_Poligon)

    def test_delete_polygon(self):
        self.geoman.draw_shape(Locators.Drow_Empty_Screen)

    def test_drag_polygon(self):
        self.geoman.draw_shape(Locators.Poligon_move_up)
        self.geoman.draw_shape(Locators.Poligon_move_left)
        self.geoman.draw_shape(Locators.Poligone_move_down)


    def test_edit_polyline(self):
        self.geoman.draw_shape(Locators.Edit_Poliline)

    def test_split_polyline_3(self):
        self.geoman.draw_shape(Locators.Split_Poliline)

    def test_delete_circle(self):
        self.geoman.draw_shape(Locators.Drow_Empty_Screen)

    def test_max_zoom(self):
        self.driver.execute_script("document.body.style.zoom='100%'")
        maxzoom = self.geoman.max_zoom()
        i = 0
        while i < 3:
            maxzoom.click()
            time.sleep(2)
            i += 1
        self.driver.execute_script("document.body.style.zoom='200%'")

    def test_min_zoom(self):
        self.driver.execute_script("document.body.style.zoom='100%'")
        minzoom = self.geoman.min_zoom()
        i = 0
        while i < 16:
            minzoom.click()
            time.sleep(2)
            i += 1
        self.driver.execute_script("document.body.style.zoom='20%'")

    def teardown(self):
        self.driver.close()
        self.driver.quit()

def main():
    mytest=Tests()
    mytest.setup()
    mytest.test_drow_circle()
    time.sleep(2)
    mytest.test_delete_circle()
    time.sleep(2)
    mytest.test_drow_polygon()
    time.sleep(2)
    mytest.test_drag_polygon()
    mytest.test_delete_polygon()
    time.sleep(2)
    mytest.test_drow_polyline()
    mytest.test_edit_polyline()
    time.sleep(2)
    mytest.test_delete_polyline()
    time.sleep(2)
    mytest.test_max_zoom()
    time.sleep(2)
    mytest.test_min_zoom()
    time.sleep(2)
    mytest.teardown()


if __name__ == '__main__':
    main()




