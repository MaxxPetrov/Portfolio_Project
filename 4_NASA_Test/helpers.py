import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE

# Main URL:
url = "https://www.nasa.gov/"

# Main Title:
title_main_page = "NASA"

# Set up random delay:


def delay_1_2():
    time.sleep(random.randint(1, 3))


# Icons XPATH:

twitter = '//img[@alt="Twitter"]'
facebook = '//img[@alt="Facebook"]'
instagram = '//img[@alt="Instagram"]'
snapchat = '//img[@alt="snapchat"]'
youtube = '//img[@alt="YouTube"]'
tumble = '//img[@alt="Tumblr"]'
pinterest = '//img[@alt="Pinterest"]'
linkedin = '//img[@alt="LinkedIn"]'
giphy = '//img[@alt="GIPHY"]'
flickr = '//img [@alt="Flickr"]'
twitch = '//img[@alt="Twitch"]'
soundcloud = '//img[@alt="Soundcloud"]'
reddit = '//img[@alt="Reddit"]'
dailymotion = '//img[@alt="Daily Motion"]'


# Assert page title:
def assert_title(smt, driver):
    assert smt == driver.title
    print("The Title of the page is:", driver.title)


# Assert Title for back page:
def assert_back_title(driver):
    assert "NASA" == driver.title
    print("Back to the main page")


# Assert title with different attribute:
def check_title(a, driver):
    assert a in driver.title
    print(f'The title of the {a} is:', driver.title)


# Function for switching windows:
def switching_windows(driver):
    wait = WebDriverWait(driver, 3)
    original_window = driver.current_window_handle
    wait.until(EC.number_of_windows_to_be(2))
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


# Function to check the logo:
def logo_check(smt, path, driver):
    wait = WebDriverWait(driver, 3)
    try:
        wait.until(
            EC.visibility_of_element_located((By.XPATH, path)))
        print(f'We have {smt} logo')
    except WDE:
        print(f'Smt is wrong with {smt} logo')
        driver.get_screenshot_as_file(f'{smt}_logo_loading_error.png')
        driver.save_screenshot(f'{smt}_logo_loading_error.png')