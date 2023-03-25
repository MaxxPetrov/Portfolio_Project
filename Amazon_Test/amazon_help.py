import time
import random
import driver
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker
from selenium.webdriver import ActionChains


main_url = "https://www.amazon.com/"
from selenium.webdriver.support import expected_conditions as EC


def check_API(driver):
    code = requests.get(driver.current_url).status_code
    if code == 200:
        print("Url has ", requests.get(driver.current_url).status_code, " as Status Code")
    else:
        print("API response code is not 200")


def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("Page has", driver.title + " as Page title")
    # Screenshot of the page
    driver.get_screenshot_as_file(f"Page {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong Title!")

        # random delay function:


def delay():
    time.sleep(random.randint(1, 5))
    delay()

    # Check "Account registration" page URL


def check_current_url(driver, current_url):
    acct_expected_url = current_url
    acct_actual_url = driver.current_url
    if acct_expected_url == acct_actual_url:
        print('"Account registration" page URL is correct:', driver.current_url)
    else:
        print('"Account registration" page URL is wrong:', driver.current_url)
