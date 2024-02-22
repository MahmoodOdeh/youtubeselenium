import unittest
import time

from infra.browser_wrapper import BrowserWrapper
from logic.menu_page import YouTubeMenu
from logic.youtube_page import YouTubePage
from logic.video_after_search_page import YouTubeSearch
from logic.page_video import YouTubePageVideo


class YoutubePageTest(unittest.TestCase):

    def test_check_title_for_search_english(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("python programing")
        time.sleep(5)
        self.assertIn("python programing", self.driver.title, "the title is not show")

    def test_check_title_for_empty_search(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("")
        time.sleep(5)
        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")

    def test_check_title_for_search_hebrew(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("עדן בן זקן")
        time.sleep(5)
        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")

    def test_check_title_for_search_arabic(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("رورو حرب")
        time.sleep(5)
        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")

    def test_play_video_from_home_page(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.press_video_home_page()
        time.sleep(5)
        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")

    def test_for_search_and_play_video(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("رورو حرب")
        time.sleep(5)
        self.Search = YouTubeSearch(self.driver)
        self.Search.play_video_after_search()
        time.sleep(15)
        self.assertIn("YouTube", self.driver.title, "The title is not correct for empty search")

    def test_for_menu_item(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        time.sleep(2)
        self.youTubePage.press_menu()
        self.shorts_item = YouTubeMenu(self.driver)
        self.shorts_item.press_shorts()
        time.sleep(5)
        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")

    def test_play_video_and_like_dislike(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver("http://youtube.com")
        self.youTubePage = YouTubePage(self.driver)
        self.youTubePage.search_flow("fifa")
        time.sleep(5)
        self.videoPlay = YouTubeSearch(self.driver)
        self.videoPlay.play_video_after_search()
        time.sleep(15)
        self.like_dislike = YouTubePageVideo(self.driver)
        self.like_dislike.click_like_button()
        time.sleep(5)
        self.like_dislike.full_screen()

        self.assertIn("YouTube", self.driver.title, "the title is not correct for empty search")
