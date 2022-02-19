from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import os

FACEBOOK_EMAIL = os.environ["FACEBOOK_EMAIL"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
TINDER_URL = "https://tinder.com/"

# todo 0 initialize webdriver
chrome_driver_path = "/Users/WilliamYu/Development/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(TINDER_URL)

time.sleep(2)

# todo 1 click login
login_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()

time.sleep(2)

# todo 2 click login with facebook
login_with_facebook_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
login_with_facebook_button.click()

time.sleep(10)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

facebook_email = driver.find_element(By.XPATH, '//*[@id="email"]')
facebook_email.send_keys(FACEBOOK_EMAIL)
facebook_password = driver.find_element(By.NAME, "pass")
facebook_password.send_keys(FACEBOOK_PASSWORD)
time.sleep(random.random())
facebook_password.send_keys(Keys.ENTER)

# switch back to base window
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)

# todo 3 input email and password of facebook

# click allow location button
location_button = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[1]')
location_button.click()

# click not allow notification anchor
not_allow_notification_anchor = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div/div/div[3]/button[2]')
not_allow_notification_anchor.click()

# click accept cookies button
accept_cookies_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[2]/div/div/div[1]/button')
accept_cookies_button.click()

time.sleep(5)

for n in range(100):
    time.sleep(random.uniform(1, 2))
    try:
        print("called")
        pick_button = driver.find_element(By.XPATH, '//*[@id="o41285377"]/div/div[1]/div/main/div[1]/div/'
                                                    'div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        pick_button.click()
    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(random.uniform(2, 3))

driver.quit()