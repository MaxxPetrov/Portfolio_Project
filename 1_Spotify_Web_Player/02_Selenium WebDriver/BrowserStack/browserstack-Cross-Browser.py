import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchWindowException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from UnitTest import helpers as Hp
import my_key  # Import BrowserStack Key


class Spotify_Web_Player(unittest.TestCase):

    def setUp(self):
        desired_cap = {
            'os_version': 'Big Sur',
            'os': 'OS X',
            'browser': 'Safari',
            'browser_version': '14.1',
            'name': 'UnitTest_Spotify_Web_player',  # test name
            'build': 'browserstack-build-1'
        }
        key = my_key.key
        desired_cap['acceptSslCerts'] = True
        self.driver = webdriver.Remote(command_executor=key,
                                       desired_capabilities=desired_cap)
        self.driver.maximize_window()

    def test01_Pos_LogIn(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***********************************************************\n"
              "TEST 1 - LOG IN\n"
              "***********************************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 10)  # Create variable for wait.until
        # Check that an elements are present and visible on the Home page
        Hp.home_page_elements(driver, "Home", "Search", "Your Library",)
        Hp.delay()
        # Log in:
        driver.find_element(By.XPATH, Hp.btn_login).click() # Click on "Log in" button
        Hp.delay()
        driver.find_element(By.ID, "login-username").send_keys(Hp.user_email)  # put email
        driver.find_element(By.ID, 'login-password').send_keys(Hp.user_pass)  # put password
        driver.find_element(By.XPATH, '//*[@class="Type__TypeElement-goli3j-0 dmuHFl sc-hKwDye eKDPqH"]').click()  # click "Log in"
        print('Log in was successful ')
        Hp.delay()
        Hp.assert_title(driver, "Spotify – Web Player") # Verify Homepage Title
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.m_home)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.m_home)))
        print('"Home" menu is visible and clickable')
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.m_search)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.m_search)))
        print('"Search" menu is visible and clickable')
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"Your Library" menu is visible and clickable')
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_songs)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_songs)))
        print('"Liked Songs" menu is visible and clickable')
        driver.find_element(By.XPATH, '//*[@class="odcjv30UQnjaTv4sylc0"]').click()  # click on account menu
        driver.find_element(By.XPATH, "//span[contains(text(),'Profile')]").click()  # clik on the profile menu
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'rasacet733')]")))
            print("Login successful")
            driver.get_screenshot_as_file("Profile menu page.png")
        except TimeoutException:
            print("Login failed")
        if not "Login failed." in driver.page_source:
            print("TEST 1 PASS")
        else:
            print("Login failed.\nTEST 3 FAIL")
            raise Exception("Login failed.\n TEST 3 FAIL ")

        driver.close()

    def test02_Pos_Search_module(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 2 - SEARCH MODULE\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.m_search)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.m_search)))
        print('"Search" menu is visible and clickable')
        Hp.delay()
        # Testing "Search" module
        driver.find_element(By.XPATH, Hp.m_search).click()  # click on "Search" menu
        Hp.delay()
        driver.find_element(By.XPATH, Hp.fld_search).send_keys(Hp.n_artist)  # send artist name for searching
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@class="Chip__ChipComponent-ry3uox-0 kiZqpO"]').click() # click on "Artist" option under search field
        time.sleep(3)
        driver.find_element(By.LINK_TEXT, Hp.n_artist)  # Check that the found right artist
        print("The artist was successfully found")
        time.sleep(3)
        driver.find_element(By.XPATH, Hp.fld_search).clear()  # clear searching field
        driver.find_element(By.XPATH, Hp.fld_search).send_keys(Hp.n_track_1)  # send song for searching
        Hp.delay()
        driver.find_element(By.XPATH,
                            '//*[@class="Chip__ChipComponent-ry3uox-0 kiZqpO"]').click()  # click on "Songs" option under search field
        Hp.delay()
        driver.find_element(By.LINK_TEXT, Hp.n_track_1)
        print("The song was successfully found")
        Hp.delay()
        driver.find_element(By.XPATH, Hp.fld_search).clear()  # clear searching field
        driver.find_element(By.XPATH, Hp.fld_search).send_keys(Hp.n_album)  # send album name for searching
        Hp.delay()
        driver.find_element(By.LINK_TEXT, Hp.n_album)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.n_album)))
        print("The album was successfully found")
        print('TEST 2 PASS')

        driver.close()

    def test03_Pos_Create_New_Playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 3 - CREATE NEW PLAYLIST\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.crt_playlist)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.crt_playlist)))
        print('"Create playlist" menu visible and clickable')
        Hp.delay()
        driver.find_element(By.XPATH, Hp.crt_playlist).click()  # create new playlist
        Hp.delay()
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()
        Hp.delay()
        Hp.assert_title(driver, "Spotify – Your Library")  # Verify title "Your Library" page
        # Check that New playlist was created
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@title="My Playlist #1"]')))
            print("Playlist was created:")
            print(driver.find_element(By.XPATH, '//*[@title="My Playlist #1"]').text)
            driver.get_screenshot_as_file("My Playlist #1.png")
        except TimeoutException:
            print("My Playlist #1 was not found")
        if not "You haven't saved My Playlist yet." in driver.page_source:
            print("TEST 3 PASS")
        else:
            print("You haven't saved My Playlist yet.\nTEST 3 FAIL")
            raise Exception("You haven't saved My Playlist yet.\n TEST 3 FAIL")

        driver.close()

    def test04_Pos_Rename_Playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 4 - RENAME PLAYLIST (Chrome Browser)\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"My library" menu is visible and clickable')
        Hp.delay()
        # Rename playlist
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@title="My Playlist #1"]').click()  # find and click on "Playlist" menu
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@data-testid="more-button"]').click()  # find and click on "More options" button
        Hp.delay()
        driver.find_element(By.XPATH,
                           "//span[contains(text(),'Edit details')]").click()  # find and click on "More options" button
        Hp.delay()
        driver.find_element(By.XPATH,
                            '//*[@data-testid="playlist-edit-details-name-input"]').clear()  # find and click on "More options" button
        Hp.delay()
        driver.find_element(By.XPATH,
                           '//*[@data-testid="playlist-edit-details-name-input"]').send_keys(Hp.rnm_playlist)  # send new playlist's name

        driver.find_element(By.XPATH,
                            '//*[@data-testid="playlist-edit-details-save-button"]').click()  # save new playlist name
        Hp.delay()
        # Check that the playlist name was successfully updated
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'My Beatles playlist')]")))
            print("My playlist name has been successfully updated:")
            print(driver.find_element(By.XPATH, "//h1[contains(text(),'My Beatles playlist')]").text)
            print("TEST 4 PASS")
            driver.get_screenshot_as_file("Updated playlist.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 4 FAIL")
            raise Exception("Second new address is NOT updated\nTEST 4 FAIL")

        driver.close()

    def test05_Pos_Add_song_to_playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 5 - ADD SONG TO PLAYLIST\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        time.sleep(3)
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"My library" menu is visible and clickable')
        Hp.delay()
        # Add song to playlist
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, "//div[contains(text(),'My Beatles playlist')]").click()  # click on the playlist
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@role="searchbox"]').send_keys(Hp.n_track_1)  # send name of song to the search field
        Hp.delay()
        driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/button[1]").click()  # click button "add" song to the current playlist
        Hp.delay()
        # Check the song has been added to the playlist and take a screenshot.
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@class="LunqxlFIupJw_Dkx6mNx"]').click()
        time.sleep(3)
        # Check the song has been successfully added to the playlist
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'Let It Be - Remastered 2009')]")))
            print("Song added to playlist:")
            print(driver.find_element(By.XPATH, "//div[contains(text(),'Let It Be - Remastered 2009')]").text)
            print("TEST 5 PASS (Chrome Browser)")
            driver.get_screenshot_as_file("Updated playlist.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 5 FAIL")
            raise Exception("Second new address is NOT updated\nTEST 5 FAIL")

        driver.close()

    def test06_Pos_Delete_song_from_playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 6 - REMOVE SONG FROM PLAYLIST\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"My library" menu is visible and clickable')
        Hp.delay()
        # Delete song from playlist
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, "//div[contains(text(),'My Beatles playlist')]").click()  # click on the playlist
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@aria-label="More options for Let It Be - Remastered 2009 by The Beatles"]').click()  # click on The button "More options" for playlist
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Remove from this playlist')]").click()  # clik on menu 'Remove from this playlist'
        print("Song successfully removed from playlist\n"
              "TEST 6 PASS")
        #  Delete the playlist completely for the next tests in other browsers
        Hp.delay()
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, "//div[contains(text(),'My Beatles playlist')]").click()  # click on the playlist
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@aria-label="More options for My Beatles playlist"]').click() # click on The button "More options" for playlist
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Delete')]").click()  # clik on button delete playlist
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Delete')]").click()  # confirm delete
        Hp.delay()

        driver.close()

    def test07_Pos_Follow_to_an_existing_playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 7 - FOLLOW TO AN EXISTING PLAYLIST\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"My library" menu is visible and clickable')
        Hp.delay()
        # Add existing playlist
        driver.find_element(By.XPATH, Hp.m_search).click()  # click on "Search" menu
        Hp.delay()
        driver.find_element(By.XPATH, Hp.fld_search).send_keys(Hp.n_artist)  # send artist name for searching
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Playlists')]").click() # click on "Playlists" option under search field
        Hp.delay()
        driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]").click()
        Hp.delay()
        driver.find_element(By.XPATH,
                            "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]").click()
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Add to Your Library')]").click()
        Hp.delay()
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        # Check that an existing playlist has been successfully added to the library
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@title="The beatles greatest hits"]')))
            print("Playlist added to the library:")
            print(driver.find_element(By.XPATH, '//*[@title="The beatles greatest hits"]').text)
            print("TEST 7 PASS")
            driver.get_screenshot_as_file("Updated playlist.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 7 FAIL")
            raise Exception("Second new address is NOT updated\nTEST 7 FAIL")

        driver.close()

    def test08_Pos_Unfollow_to_an_existing_playlist(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 8 - UNFOLLOW TO AN EXISTING PLAYLIST\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.login(driver)  # Log in exist account
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, Hp.m_library)))
        wait.until(EC.element_to_be_clickable((By.LINK_TEXT, Hp.m_library)))
        print('"My library" menu is visible and clickable')
        Hp.delay()
        # Add existing playlist
        driver.find_element(By.LINK_TEXT, Hp.m_library).click()  # find and click on "my library" menu
        Hp.delay()
        driver.find_element(By.XPATH, '//*[@title="The beatles greatest hits"]').click()
        Hp.delay()
        driver.find_element(By.XPATH, "//body/div[@id='main']/div[1]/div[2]/div[3]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/main[1]/div[1]/section[1]/div[2]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/button[2]/*[1]").click()
        Hp.delay()
        driver.find_element(By.XPATH, "//span[contains(text(),'Remove from Your Library')]").click()
        Hp.delay()
        print("Playlist successfully removed from library\n"
              "TEST 8 PASS")

        driver.close()

    def test09_Neg_Login_with_invalid_email(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 9 - LOG IN WITH INVALID EMAIL (Chrome Browser)\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.btn_login)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.btn_login)))
        print('Button "Log In" is visible and clickable')
        Hp.delay()
        # Log in with invalid email
        Hp.login_inv_email(driver)
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")))
            print("Login with invalid email address failed:")
            print(driver.find_element(By.XPATH, "//span[contains(text(),'Incorrect username or password.')]").text)
            print("TEST 9 PASS (Chrome Browser)")
            driver.get_screenshot_as_file("Invalid email Log in.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 9 FAIL (Chrome Browser)")
            raise Exception("Second new address is NOT updated\nTEST 9 FAIL (Chrome Browser)")

        driver.close()

    def test_010_Neg_Login_with_invalid_password(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 10 - LOG IN WITH INVALID PASSWORD\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.btn_login)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.btn_login)))
        print('Button "Log In" is visible and clickable')
        Hp.delay()
        # Log in with invalid email
        Hp.login_inv_password(driver)
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")))
            print("Login with invalid email address failed:")
            print(driver.find_element(By.XPATH, "//span[contains(text(),'Incorrect username or password.')]").text)
            print("TEST 10 PASS")
            driver.get_screenshot_as_file("Invalid email Log in.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 10 FAIL")
            raise Exception("Second new address is NOT updated\nTEST 10 FAIL")

        driver.close()

    def test_011_Neg_Login_with_empty_email_field(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 11 - LOG IN WITH EMPTY EMAIL FIELD\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.btn_login)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.btn_login)))
        print('Button "Log In" is visible and clickable')
        Hp.delay()
        # Log in with invalid email
        Hp.login_empt_email(driver)
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")))
            print("Login with invalid email address failed:")
            print(driver.find_element(By.XPATH, "//span[contains(text(),'Incorrect username or password.')]").text)
            print("TEST 11 PASS")
            driver.get_screenshot_as_file("Invalid email Log in.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 11")
            raise Exception("Second new address is NOT updated\nTEST 11")

        driver.close()

    def test_012_Neg_Login_with_empty_password_field(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 12 - LOG IN WITH EMPTY PASSWORD FIELD\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.btn_login)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.btn_login)))
        print('Button "Log In" is visible and clickable')
        Hp.delay()
        # Log in with invalid email
        Hp.login_empt_password(driver)
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")))
            print("Login with invalid email address failed:")
            print(driver.find_element(By.XPATH, "//span[contains(text(),'Incorrect username or password.')]").text)
            print("TEST 12 PASS")
            driver.get_screenshot_as_file("Invalid email Log in.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 12")
            raise Exception("Second new address is NOT updated\nTEST 12 FAIL")

        driver.close()

    def test_013_Ad_Hoc_Login_with_invalid_email(self):
        driver = self.driver
        driver.get(Hp.main_url)  # open URL - home page
        # driver.set_window_size(1200, 800)  # Set another Window Size
        print("***************************************\n"
              "TEST 13 - LOG IN WITH AD HOC EMAIL\n"
              "***************************************")
        Hp.check_API_code(driver)  # Check API response code
        Hp.assert_title(driver, "Spotify – Web Player")  # Verify Homepage Title
        wait = WebDriverWait(driver, 5)  # Create variable for wait.until
        Hp.delay()
        # Check "Spotify – Web Player" page functionality
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.logo_sptf)))
        print("Spotify logo is visible")
        Hp.delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.btn_login)))
        wait.until(EC.element_to_be_clickable((By.XPATH, Hp.btn_login)))
        print('Button "Log In" is visible and clickable')
        Hp.delay()
        # Log in with invalid email
        Hp.login_adhoc_email(driver)
        Hp.delay()
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Incorrect username or password.')]")))
            print("Login with invalid email address failed:")
            print(driver.find_element(By.XPATH, "//span[contains(text(),'Incorrect username or password.')]").text)
            print("TEST 13 PASS (Chrome Browser)")
            driver.get_screenshot_as_file("Invalid email Log in.png")
        except TimeoutException:
            print("Second new address is NOT updated\nTEST 13")
            raise Exception("Second new address is NOT updated\nTEST 13 FAIL")

        driver.close()

    def tearDown(self):
        self.driver.quit()  # Close the browser.

if __name__ == "__main__":
    unittest.main()
