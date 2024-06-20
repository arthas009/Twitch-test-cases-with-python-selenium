import unittest
from utils.driver_setup import get_driver
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_page import TwitchSearchPage
from pages.twitch_streamer_page import TwitchStreamerPage

class TestTwitch(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.home_page = TwitchHomePage(self.driver)
        self.search_page = TwitchSearchPage(self.driver)
        self.streamer_page = TwitchStreamerPage(self.driver)

    def test_search_starcraft(self):
        self.home_page.go_to_home_page()
        self.home_page.click_search_icon()
        self.search_page.input_search_query("StarCraft II")
        self.search_page.scroll_down(2)
        self.streamer_page.select_streamer()
        self.streamer_page.take_screenshot("streamer_screenshot.png")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
