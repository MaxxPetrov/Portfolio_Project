# Helpers file for project Spotify (Playlist)
import time
import random
import requests
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Set main variables
# URL - home page
main_url = "https://open.spotify.com/"
# User's E-mail
user_email = "rasacet733@charav.com"
# Invalid email
inv_email = "mail@.com"
# Ad Hoc email
adhoc_email = "test@mail.comtest@mail.com"

# User's password
user_pass = "rasacet733!"  # type your user's password for account
# Invalid password
inv_passw = "123456"
# profile name
profile_name = "rasacet733"
# Playlist rename
rnm_playlist = "My Beatles playlist"

# MOST OFTEN USED X-PATHs

# Log in button
btn_login = '//*[@class="ButtonInner-sc-14ud5tc-0 kuwYvr encore-inverted-light-set"]'
# Logo Spotify
logo_sptf = '//*[@class="fwTMCeAaUoWDj9WcQbgy"]'
# menu "Home"
m_home = '//*[@class="Svg-ytk21e-0 eqtHWV home-active-icon"]'
# menu "Search"
m_search = '//*[@class="Svg-ytk21e-0 eqtHWV search-icon"]'
# menu "Your Library" By.LINK_TEXT
m_library = 'Your Library'
# menu "Liked Songs" By.LINK_TEXT
m_songs = 'Liked Songs'
# menu "Create Playlist"
crt_playlist = '//*[@data-testid="create-playlist-button"]'
# "Search" field
fld_search = '//*[@class="Type__TypeElement-goli3j-0 iTnRIT QO9loc33XC50mMRUCIvf"]'
# Artist name
n_artist = 'The Beatles'
# Track name
n_track_1 = 'Let It Be - Remastered 2009'
# Album name
n_album = 'Abbey Road'



# Set random delay
def delay():
    time.sleep(random.randint(2, 4))

# Check API response code
def check_API_code(driver):
    code = requests.get(main_url).status_code
    if code == 200:
        print('Url has ', requests.get(main_url).status_code, ' as API status code')
    else:
        print('API response code is not 200')

# Verify Pages Title
def assert_title (driver, title,):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("Page has", driver.title + " as page title")
    delay()
    # Screenshot of the page
    driver.get_screenshot_as_file(f"Page {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong Title!")

# Check that an elements are present and visible on the Home page
def home_page_elements(driver, text1, text2, text3,):
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), text1)]")))
            print(f"Text {text1} is visible!")
        except TimeoutException:
            print("Loading text too much time!")
            driver.get_screenshot_as_file("Loading text too much time.png")
        element = driver.find_element(By.LINK_TEXT, text2)
        if text2 in driver.page_source:
            print(f"LinkText {text2} has attribute " + element.get_attribute("href"))
        else:
            print(f"Page don't have LinkText = {text2}")
        if not text2 in driver.page_source:
            raise Exception("Link Text is wrong!")

        element_2 = driver.find_element(By.LINK_TEXT, text3)
        if text3 in driver.page_source:
            print(f"LinkText {text3} has attribute " + element_2.get_attribute("href"))
        else:
            print(f"Page don't have LinkText = {text3}")
        if not text3 in driver.page_source:
            raise Exception("Link Text is wrong!")

def login(driver):
    # Set wait until button 'Login' will be clickable
    wait = WebDriverWait(driver, 10)
    delay()
    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").send_keys(user_email)  # put email
    driver.find_element(By.ID, 'login-password').send_keys(user_pass)  # put password
    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"

def login_inv_email(driver):

    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").send_keys(inv_email)  # put email
    driver.find_element(By.ID, 'login-password').send_keys(user_pass)  # put password
    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"

def login_inv_password(driver):

    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").send_keys(user_email)  # put email
    driver.find_element(By.ID, 'login-password').send_keys(inv_passw)  # put password
    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"

def login_empt_email(driver):

    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").click()
    driver.find_element(By.ID, 'login-password').send_keys(user_pass)  # put password
    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"

def login_empt_password(driver):

    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").send_keys(user_email)  # put email

    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"

def login_adhoc_email(driver):

    driver.find_element(By.XPATH, btn_login).click()  # Click on "Log in" button
    delay()
    driver.find_element(By.ID, "login-username").send_keys(adhoc_email)  # put email
    driver.find_element(By.ID, 'login-password').send_keys(user_pass)  # put password
    driver.find_element(By.XPATH,
                        '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"


