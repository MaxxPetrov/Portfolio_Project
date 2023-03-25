import time

from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread

from Headless import fake

load_dotenv()
# you need to replace second BROWSERSTACK_USERNAME and BROWSERSTACK_ACCESS_KEY for your credentials
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "maxpower_3ITmGJ"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "FEksQkDfsrKZRes969tx"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Firefox",
        "browserVersion": "latest-beta",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python sample parallel",  # test name
        "buildName": 'my_test',  # Your tests will be organized within this build
    },

]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        driver.get("https://www.amazon.com/")
        time.sleep(3)
        wait = WebDriverWait(driver, 3)
        try:
            assert driver.title == "Amazon.com. Spend less. Smile more."
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)

        driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys(fake.city())
        driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']").click()
        driver.find_element(By.XPATH, "//a[contains(@class,'a-button-text')]").click()
        driver.find_element(By.XPATH, "//input[@type='text'][contains(@id,'name')]").send_keys(fake.name())
        driver.find_element(By.XPATH, "//input[@type='email'][contains(@id,'email')]").send_keys(fake.email())

        fakepassword = fake.password()
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys(fakepassword)

        # password_confirm
        driver.find_element(By.ID, "ap_password_check").send_keys(fakepassword)
        driver.find_element(By.XPATH, "//input[@id='continue']")
        driver.execute_script("window.history.go(-2)")
        time.sleep(3)
        acct_reg_expected_title = "Amazon.com. Spend less. Smile more."
        acct_reg_actual_title = driver.title
        if acct_reg_expected_title == acct_reg_actual_title:
            print('"Account registration" page Title is correct:', driver.title)
        else:
            print('"Account registration" page Title is wrong:', driver.title)
        driver.find_element(By.XPATH, "//i[contains(@class,'hm-icon nav-sprite')]").click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'trending')]")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/gp/bestsellers/?ref_"
                                                         "=nav_em_cs_bestsellers_0_1_1_2']")))
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/gp/new-releases/?ref_=nav_em_cs_newreleases_0_1_1_3'] "))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'Movers & Shakers')]")))
        driver.find_element(By.XPATH, "//a[contains(@data-ref-tag,'nav_em_1_1_1_6')]").click()
        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, "//a[@href='/Amazon-Video/b?node=2858778011&ref_=nav_em__aiv_0_2_2_2'] ").click()
        driver.implicitly_wait(4)
        try:
            assert driver.title == "Amazon.com: Prime Video: Prime Video"
            print("Title is Correct. Current Title is:", driver.title)
        except AssertionError:
            print("Title is different. Current Title is:", driver.title)
        driver.find_element(By.XPATH, "//input[contains(@type,'text')]").send_keys("The End of Testing :)")
        time.sleep(5)
    except NoSuchElementException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
        # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()
