# mouse = Controller()
# while True:
#     current_mouse_position = mouse.position
#     print(current_mouse_position)
# location = json_c.location    #json_c.location["x"]
# x = location["x"]
# y = location["y"]
# current_mouse_position=mouse.position
# print(current_mouse_position)
# action.move_by_offset(2423, 877).context_click().perform()

# source=driver.find_elements_by_xpath('//*[@id="box3"]')[0]
# target=driver.find_elements_by_xpath('//*[@id="box103"]')[1]
#
# action=ActionChains(driver)
# action.drag_and_drop(source, target).perform()


# action = ActionChains(self.driver)
# x=-44
# y=10
# action.move_by_offset(x, y).click().perform()
# source=driver.find_elements_by_xpath('//*[@id="box3"]')[0]
# target=driver.find_elements_by_xpath('//*[@id="box103"]')[1]
#
# action=ActionChains(driver)
# action.drag_and_drop(source, target).perform()


# action = ActionChains(self.driver)
# x=-44
# y=10
# action.move_by_offset(x, y).click().perform()

# circle_location_locator = "//div[@id='map']/div/div[4]/div[2]"
# circle_location = WebDriverWait(self.driver, 10).until(
#     EC.visibility_of_all_elements_located((By.XPATH, circle_location_locator)))
# circle_loc = circle_location[0]
# circle_loc.click()
#
# circle_location_2_locator = "//div[@id='map']/div/div[4]/div[2]"
# circle_location_2 = WebDriverWait(self.driver, 50).until(
#     EC.visibility_of_all_elements_located((By.XPATH, circle_location_2_locator)))
# circle_location2 = circle_location_2[0]
# circle_location2.click()
#
# circle_location_3_locator = "//div[@id='map']/div[2]/div/div[2]/div[5]/a/div"
# circle_location_3 = WebDriverWait(self.driver, 50).until(
#     EC.visibility_of_all_elements_located((By.XPATH, circle_location_3_locator)))
# location_3 = circle_location_3[0]
# location_3.click()


# move_to_element_chrome(self.driver, circle_location, display_scaling=100, chrome_info_bar_shown=True)

# self.driver.execute_script('arguments[0].removeAttribute(\"readonly\")', json_c)
# self.driver.execute_script('arguments[0].setAttribute("value", "' + "read" + '")', json_c);
# javaScript = "document.getElementsByXpath('" + json_code_locator + "')[0].removeAttribute('readonly');"
# self.driver.execute_script(javaScript)


# json_to_string2 = json.dumps(Draw_Circle)
# json_to_string = json.dumps(Draw_Circle, sort_keys=True, separators=('\n', '\r'))

# circle_button = self.get_circle_button()
# circle_button.click()
# action.move_to_element(json_c).click().perform()
# json_code_locator = "//*[@id='__layout']/div/main/div/div[2]/div[2]/div[1]/div/div/div/div[6]/div[1]/div/div/div/div[5]"
# json_code = WebDriverWait(self.driver, 50).until(
#     EC.visibility_of_all_elements_located((By.XPATH, json_code_locator)))

# with open("C:\\Alex\\My_Projects\\silverlight-tests-with-jmeter\my-app\\node_modules\\typescript\\ThirdPartyNoticeText.txt", 'r') as f:
#     lines = f.readlines()
#     parselines = re.split(r'^$\n|\r|\t|,|\\|-|\'', str(lines))
#
#     resp = str(lines).count("The")
#     result = str(lines).index("The")
#     for line in parselines:
#         if line:
#             if line != "n" and line != "'" and line != ' ' and line != "":
#                 if "conforming" in line:
#                     res = len(re.findall(r'\w+', line))
#                     count = line.count("The")
#                     print(count)
#                     print(res)
#                     print(line)
# def press_drow_circle(self):
    #     action = ActionChains(self.driver)
    #     json_c = self.get_json_text_box()
    #     action.move_to_element(json_c).click().perform()
    #     text = json_c.text
    #     while text != "1":
    #         action.move_to_element(json_c).send_keys(Keys.DELETE).perform()
    #         action.move_to_element(json_c).send_keys(Keys.UP).perform()
    #         text = json_c.text
    #
    #     action.send_keys(Draw_Circle).perform()
    #
    # def press_drow_Poligon(self):
    #     action=ActionChains(self.driver)
    #     json_c = self.get_json_text_box()
    #     action.move_to_element(json_c).click().perform()
    #     text = json_c.text
    #     while text != "1":
    #         action.move_to_element(json_c).send_keys(Keys.DELETE).perform()
    #         action.move_to_element(json_c).send_keys(Keys.UP).perform()
    #         text = json_c.text
    #
    #     action.send_keys(Draw_Poligon).perform()
    #
    # def press_drow_polyline(self):
    #     action=ActionChains(self.driver)
    #     json_c=self.get_json_text_box()
    #     action.move_to_element(json_c).click().perform()
    #     text = json_c.text
    #     while text != "1":
    #         action.move_to_element(json_c).send_keys(Keys.DELETE).perform()
    #         action.move_to_element(json_c).send_keys(Keys.UP).perform()
    #         text = json_c.text
    #
    #     action.send_keys(Draw_Poliline).perform()
    #
    # def press_delete_circle(self):
    #     action = ActionChains(self.driver)
    #     json_c = self.get_json_text_box()
    #     action.move_to_element(json_c).click().perform()
    #     text = json_c.text
    #     while text != "1":
    #         action.move_to_element(json_c).send_keys(Keys.DELETE).perform()
    #         action.move_to_element(json_c).send_keys(Keys.UP).perform()
    #         text = json_c.text
    #
    #     action.send_keys(Drow_Empty_Creen).perform()
    #     self.driver.refresh()
# action.move_to_element(json_c).send_keys(Keys.CONTROL + "a")
# action.move_to_element(json_c).send_keys(Keys.DELETE)
# action.move_to_element(json_c).send_keys(u'\ue009' + u'\ue003')
