from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_driver():
    mobile_emulation = {"deviceName": "Pixel 2"}
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver
