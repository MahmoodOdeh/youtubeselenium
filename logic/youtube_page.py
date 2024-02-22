import time

from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

from infra.base_page import BasePage


class YouTubePage(BasePage):
    SEARCH_INPUT = (By.XPATH, "//input[@id='search']")
    VIDEO_PLAY_HOME_PAGE = (By.XPATH, "//a[@id='thumbnail'][1]")
    MENU = (By.ID, "guide-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.search_input = self._driver.find_element(*self.SEARCH_INPUT)
        self.video_play_home_page = self._driver.find_elements(*self.VIDEO_PLAY_HOME_PAGE)
        self.menu = self._driver.find_element(*self.MENU)

    def fill_search_input(self, text):
        self.search_input.send_keys(text)

    def press_enter_search_input(self):
        self.search_input.send_keys(Keys.RETURN)

    def search_flow(self, text):
        self.fill_search_input(text)
        self.press_enter_search_input()

    def press_video_home_page(self):
        self.video_play_home_page[1].click()

    def press_menu(self):
        self.menu.click()
