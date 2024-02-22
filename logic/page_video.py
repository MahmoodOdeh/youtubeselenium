from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class YouTubePageVideo(BasePage):
    LIKE_BUTTON = (By.CSS_SELECTOR, "button[title*='I like this']")
    DISLIKE_BUTTON = (By.XPATH, "//button[@aria-label='Dislike this video']")
    FULLSCREEN_BUTTON = (By.XPATH, "//div[@id='movie_player']//button[@class='ytp-fullscreen-button ytp-button']")

    def __init__(self, driver):
        super().__init__(driver)
        self.like_button = self._driver.find_elements(*self.LIKE_BUTTON)
        self.dislike_button = self._driver.find_elements(*self.DISLIKE_BUTTON)
        self.full_screen = self._driver.find_elements(*self.FULLSCREEN_BUTTON)

    def click_like_button(self):
        try:
            self.like_button.click()
        except Exception as e:
            print(f"Failed to click like button: {e}")

    def click_dislike_button(self):
        self.dislike_button.click()

    def like_dislike_flow(self):
        self.click_like_button()
        self.click_dislike_button()

    def full_screen_click(self):
        self.full_screen.click()
