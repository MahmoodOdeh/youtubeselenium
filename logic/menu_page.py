from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class YouTubeMenu(BasePage):
    SHORTS = (By.XPATH, "//yt-formatted-string[text()='Shorts']")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.shorts_item = self._driver.find_element(*self.SHORTS)

    def press_shorts(self):
        self.shorts_item.click()
