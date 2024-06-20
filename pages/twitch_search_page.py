from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage

class TwitchSearchPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[type="text"]')

    def input_search_query(self, query):
        search_input = self.wait_for_element(*self.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)
    
    def scroll_down(self, times=2):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(times):
            body.send_keys(Keys.PAGE_DOWN)
