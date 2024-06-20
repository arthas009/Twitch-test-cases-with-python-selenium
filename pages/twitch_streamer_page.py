from selenium.webdriver.common.by import By
from .base_page import BasePage

class TwitchStreamerPage(BasePage):
    def select_streamer(self):
        streamers = self.driver.find_elements(By.CSS_SELECTOR, 'a[data-test-selector="preview-card-titles__primary-link"]')
        if streamers:
            streamers[0].click()
    
    def take_screenshot(self, file_path):
        self.driver.save_screenshot(file_path)
