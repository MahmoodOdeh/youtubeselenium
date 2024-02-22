from selenium import webdriver
from selenium.webdriver.common.by import By


class BrowserWrapper:

    def __init__(self):
        self.driver = None

    def get_driver(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        return self.driver
