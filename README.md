markdown
Copy code
# Twitch Test Automation

This project automates a series of actions on the mobile version of Twitch using pytest as the test runner.

## Prerequisites

- Python 3.x
- ChromeDriver
- Google Chrome

## Installation

1. Clone the repository.
2. Install the required packages:
pip install -r requirements.txt
Ensure you have ChromeDriver installed and it's in your PATH. You can download it from here.

## Running the Tests
Open a terminal or command prompt.
Navigate to the project directory.

Run the tests using pytest:
pytest tests/

## Test Structure
pages/: Contains the Page Object Models for different pages of the application.
tests/: Contains the test cases.
utils/: Contains utility functions like driver setup.
## Test Case
The test case performs the following actions:

Opens the Twitch home page.
Clicks on the search icon.
Inputs "StarCraft II".
Scrolls down twice.
Selects the first streamer.
Waits until the streamer page is fully loaded and takes a screenshot.

## Explanation of Test Files
base_page.py: Contains the base page class with common functions used by other page classes.
twitch_home_page.py: Contains the page object for the Twitch home page with methods to interact with elements on the home page.
twitch_search_page.py: Contains the page object for the Twitch search page with methods to interact with elements on the search page.
twitch_streamer_page.py: Contains the page object for the Twitch streamer page with methods to interact with elements on the streamer page.
test_twitch.py: Contains the test case that uses the page objects to perform the actions.
driver_setup.py: Contains the setup for the Selenium WebDriver.
