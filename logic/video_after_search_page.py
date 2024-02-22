from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class YouTubeSearch(BasePage):
    VIDEO_PLAY_AFTER_SEARCH = (By.XPATH, "(//ytd-video-renderer)[1]")

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver
        self.video_play_after_search = self._driver.find_element(*self.VIDEO_PLAY_AFTER_SEARCH)

    def play_video_after_search(self):
        self.video_play_after_search.click()

    def get_page_title(self):
        return self._driver.title
