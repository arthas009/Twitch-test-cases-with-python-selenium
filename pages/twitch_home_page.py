from selenium.webdriver.common.by import By
from .base_page import BasePage

class TwitchHomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, 'button[data-a-target="search-input"]')

    def go_to_home_page(self):
        self.driver.get("https://m.twitch.tv/")
    
    def click_search_icon(self):
        self.wait_for_element(*self.SEARCH_ICON).click()
