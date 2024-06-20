# Twitch Test Automation

This project automates a series of actions on the mobile version of Twitch.

## Prerequisites

- Python 3.x
- ChromeDriver
- Google Chrome

## Installation

1. Clone the repository.
2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the tests:

```bash
python -m unittest discover -s tests
```

## Test Structure

- `pages/`: Contains the Page Object Models for different pages of the application.
- `tests/`: Contains the test cases.
- `utils/`: Contains utility functions like driver setup.

## Test Case

The test case performs the following actions:

1. Opens the Twitch home page.
2. Clicks on the search icon.
3. Inputs "StarCraft II".
4. Scrolls down twice.
5. Selects the first streamer.
6. Waits until the streamer page is fully loaded and takes a screenshot.
