import pytest
from utils.driver_setup import get_driver
from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_page import TwitchSearchPage
from pages.twitch_streamer_page import TwitchStreamerPage

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search_starcraft(driver):
    home_page = TwitchHomePage(driver)
    search_page = TwitchSearchPage(driver)
    streamer_page = TwitchStreamerPage(driver)

    home_page.go_to_home_page()
    home_page.click_search_icon()
    search_page.input_search_query("StarCraft II")
    search_page.scroll_down(2)
    streamer_page.select_streamer()
    streamer_page.take_screenshot("streamer_screenshot.png")
