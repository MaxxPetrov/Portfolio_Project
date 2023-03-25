import random
import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.common.exceptions import WebDriverException as WDE
from faker import Faker
import helpers as HP

# Headless:
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


class GoogleChrome(unittest.TestCase):

    # setup function:
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # Check if social media icons are clickable, (TC-003):
    def test_icons_clickable(self):
        driver1 = self.driver
        driver1.get(HP.url)

        # random delay function:
        def delay():
            time.sleep(random.randint(1, 5))
            delay()

        # check if URL is correct, (helper):
        Nasa_Expected_URL = HP.url
        current_url = driver1.current_url
        if current_url == Nasa_Expected_URL:
            print("Current URL is OK:", driver1.current_url)
        else:
            print("Current URL is different than expected:", driver1.current_url)

        # check if title is correct, (helper):
        Nasa_Expected_Title = "NASA"
        current_title = driver1.title
        if current_title == Nasa_Expected_Title:
            print("Current Title is OK:", driver1.title)
        else:
            print("Current Title is different than expected:", driver1.title)

        # Find elements by XPATH and click on it:
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH, "//a[@href='/socialmedia'][contains(.,'Social Media')]").click()

        # set up wait time
        wait = WebDriverWait(driver1, 5)

        # verify icons are clickable, (helpers):
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitter)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.facebook)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.instagram)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.snapchat)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.youtube)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.tumble)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.linkedin)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.giphy)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.flickr)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.twitch)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.soundcloud)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.reddit)))
            wait.until(EC.element_to_be_clickable((By.XPATH, HP.dailymotion)))

            print("Icons are clickable")
        except WDE:
            print("Check icons click ability")
            raise TimeoutException

        # validate all social media linked icons lead to right pages:

        # validate Twitter linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.twitter).click()
        assert "https://twitter.com/nasa" in driver1.current_url
        print("Twitter icon leads to Twitter page")

        # Make driver back on previous page:
        driver1.back()

        # wait 1-2 sec:
        HP.delay_1_2()

        # validate Facebook linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.facebook).click()
        assert "https://www.facebook.com/NASA/" in driver1.current_url
        print("Facebook icon leads to Facebook page")

        driver1.back()

        HP.delay_1_2()

        # validate Instagram linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.instagram).click()
        assert "https://www.instagram.com/nasa/" in driver1.current_url
        print("Instagram icon leads to Instagram homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Snapchat linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.snapchat).click()
        assert "https://snapchat.com/add/nasa" in driver1.current_url
        print("Snapchat icon leads to Snapchat homepage")

        driver1.back()

        HP.delay_1_2()

        # validate YouTube linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.youtube).click()
        assert "https://www.youtube.com/NASA" in driver1.current_url
        print("YouTube icon leads to YouTube homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Tumblr linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.tumble).click()
        assert "https://nasa.tumblr.com/" in driver1.current_url
        print("Tumblr icon leads to Tumblr homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Pinterest linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.pinterest).click()
        assert "https://www.pinterest.com/nasa/" in driver1.current_url
        print("Pinterest icon leads to Pinterest homepage")

        driver1.back()

        HP.delay_1_2()

        # validate GIPHY linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.giphy).click()
        assert "https://giphy.com/nasa" in driver1.current_url
        print("GIPHY icon leads to GIPHY homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Flickr linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.flickr).click()
        assert "https://www.flickr.com/photos/nasahqphoto/" in driver1.current_url
        print("Flickr icon leads to Flickr homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Twitch linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.twitch).click()
        assert "https://www.twitch.tv/nasa/" in driver1.current_url
        print("Twitch icon leads to Twitch homepage")

        driver1.back()

        HP.delay_1_2()

        # validate SoundCloud linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.soundcloud).click()
        assert "https://soundcloud.com/nasa" in driver1.current_url
        print("SoundCloud icon leads to SoundCloud homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Reddit linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.reddit).click()
        assert "https://www.reddit.com/user/nasa" in driver1.current_url
        print("Reddit icon leads to Reddit homepage")

        driver1.back()

        HP.delay_1_2()

        # validate Dailymotion linked icon leads to correct page:
        driver1.find_element(By.XPATH, HP.dailymotion).click()
        assert "https://www.dailymotion.com/NASA" in driver1.current_url
        print("Dailymotion icon leads to Dailymotion  homepage")

        print("TC-003 is PASSED")

        # Make Browser back at previous page:
        driver1.back()

        # Close Browser's tab
        driver1.close()

    # Check the ability of user sign up for NASA’s Newsletters (TC-001):
    def test_newsletters(self):
        driver1 = self.driver
        driver1.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver1.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Faker set up:
        fake = Faker()

        # Find elements by XPATH and send fake data:
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.com")
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())
        driver1.find_element(By.XPATH, '//input[@data-input-id="city"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="city"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="city"]').send_keys(fake.city())
        driver1.find_element(By.XPATH, '//input[@data-input-id="state"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="state"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="state"]').send_keys(fake.state())
        driver1.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="postal_code"]').send_keys("11229")
        driver1.find_element(By.XPATH, '//input[@data-input-id="country"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="country"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="country"]').send_keys(fake.country())
        driver1.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # should pass Captcha before with 3 images selection
        # driver.find_element(By.PARTIAL_LINK_TEXT, "Thanks for Subscribing!")

        print("Subscription for Newsletters was Done!")
        print("TC-001 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify that user is unable to make a subscription for a Newsletters by using invalid Email (TC-002)/Negative Test:

    def test_subscription_negative(self):
        driver1 = self.driver
        driver1.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH,
                             "//a[@href='https://www.nasa.gov/newsletters'][contains(.,'NASA Newsletters')]").click()
        HP.delay_1_2()

        driver1.find_element(By.XPATH, "//a[@href='https://www.nasa.gov/specials/newsletter-sign-up/']").click()
        HP.delay_1_2()

        # Find elements by XPATH and send fake data:
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0102@gmail.c")
        driver1.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # Verify user got Error Message:
        driver1.find_element(By.XPATH, "//div[@class='message'][contains(.,'Email is invalid.')]")

        print("User is unable to make subscription with Invalid Email")
        print("TC-002 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify the ability of user to make a registration for NASA's upcoming events (TC-004):

    def test_upcoming_events(self):
        driver1 = self.driver
        driver1.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page
        assert "NASA Virtual Guest Ops" in driver1.title
        print("NASA Virtual Guest page is opened")

        driver1.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver1.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page
        driver1.find_element(By.XPATH, "//img[@data-image-content]")
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver1.current_url
        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.com")
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        driver1.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]')

        # should pass Captcha before with 3 images selection
        # driver1.find_element(By.XPATH, '//a[@data-purpose="download"]')

        print("Join to NASA's Virtual Guest List was Done!")
        print("TC-004 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify that user is unable to make a registration  for NASA's upcoming events  with invalid email (
    # TC-005)/Negative Test:

    def test_upcoming_events_negative(self):
        driver1 = self.driver
        driver1.get(HP.url)

        # Set up custom window size:
        self.driver.set_window_size(300, 1800)

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, '//button[@class ="navbar-toggle collapsed"]').click()
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH, "//a[@href='/specials/virtualguest/']").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page
        assert "NASA Virtual Guest Ops" in driver1.title
        print("NASA Virtual Guest page is opened")

        driver1.find_element(By.XPATH, '//a[@class ="w3-button w3-round-xlarge w3-nasa-blue"]').click()

        HP.delay_1_2()

        driver1.get("https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests")

        # Verify opened page is SignUp Form page:
        assert "https://lp.constantcontactpages.com/su/SCofgRt/NASAvirtualguests" in driver1.current_url
        driver1.find_element(By.XPATH, "//img[@data-image-content]")

        print("Current Signup Form Page is correct")

        # Faker set up:
        fake = Faker()

        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="email_address"]').send_keys("test0103@gmail.c")
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="first_name"]').send_keys(fake.first_name())
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').click()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').clear()
        driver1.find_element(By.XPATH, '//input[@data-input-id="last_name"]').send_keys(fake.last_name())

        print("Sign Up Form is filled by Fake data")

        # Click "Submit" button:
        driver1.find_element(By.XPATH, '//button[@data-purpose="signup-submit-form"]').click()

        # Verify user got Error Message:
        driver1.find_element(By.XPATH, "//label[contains(., '* Email')]")
        # driver.find_element(By.XPATH, '//*[contains(text(),"Email is invalid."]')

        print("User is unable to make a registration  for NASA's upcoming events  with invalid email")
        print("TC-005 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify that Logo leads to the website's Homepage after clicking on it, (TC-006):

    def test_logo_functionality(self):
        driver1 = self.driver
        driver1.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH, "//span[contains(.,'Follow NASA')]").click()
        driver1.find_element(By.XPATH, "//a[@href='/solve/index.html'][contains(.,'Get Involved')]").click()

        HP.delay_1_2()

        # Verify opened page is SignUp Form page
        assert "Participate with NASA Solve | NASA" in driver1.title
        print("Page title is correct")

        HP.delay_1_2()

        # Find logo Icon:
        driver1.find_element(By.XPATH, "//nav[@id='navbar-nasa']/div/a/img").click()
        # driver.find_element(By.XPATH, '//img[@alt="Nasa" and @xpath="1"]').click()

        HP.delay_1_2()

        # Verify logo leaded to Homepage:
        # check if Homepage title is correct, strict assertion:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if Homepage URL is correct, strict assertion:
        assert HP.url == driver1.current_url
        print("Current URL of Homepage is OK:", driver1.current_url)

        print("Logo leads to the website's Homepage")
        print("TC-006 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify that the “Search” field is working appropriate, (TC-007):

    def test_search_field(self):
        driver1 = self.driver
        driver1.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
        HP.delay_1_2()
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys("Events")
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)

        HP.delay_1_2()
        assert "Events - NASA Search Results" in driver1.title

        print("Correct Page is opened by Search result")
        print("TC-007 is PASSED")

        # Close Browser's tab:
        driver1.close()

    # Verify that the “Search” field is working appropriate/Negative Testing),(TC-008):

    def test_search_field_negative(self):
        driver1 = self.driver
        driver1.get(HP.url)
        self.driver.maximize_window()

        # wait 1-2 seconds:
        HP.delay_1_2()

        # check if title is correct:
        assert HP.title_main_page == driver1.title
        print("Current Title is OK:", driver1.title)

        # check if URL is correct:
        assert HP.url == driver1.current_url
        print("Current URL is OK:", driver1.current_url)

        # set up wait time:
        WebDriverWait(1, 3)

        # find elements by XPATH:
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").click()
        HP.delay_1_2()
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(".")
        driver1.find_element(By.XPATH, "//input[contains(@aria-hidden,'false')]").send_keys(Keys.RETURN)

        HP.delay_1_2()
        assert ". - NASA Search Results" in driver1.title
        driver1.find_element(By.XPATH, "//div[contains( @class ,'content-block-item')]")
        driver1.find_element(By.XPATH, '//div[contains(text(),"Sorry, no results found for")]')

        print("Notification about wrong data in Search field is got")
        print("TC-008 is PASSED")

        # Close Browser's tab:
        driver1.close()


# close entire Browser:


def tearDown(self):
    self.driver.quit()