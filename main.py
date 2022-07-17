from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
import random
import os

FACEBOOK_EMAIL = os.environ["FACEBOOK_EMAIL"]
FACEBOOK_PASSWORD = os.environ["FACEBOOK_PASSWORD"]
TINDER_URL = "https://tinder.com/app/recs"
DAILY_WIPE_TIMES = 100

# todo 0 initialize webdriver
chrome_driver_path = "C:/Development/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(TINDER_URL)

# wait until the main page ready.
time.sleep(2)

# todo 1 click login
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log in')))
time.sleep(1)
login_button.click()
print("login button clicked.")

time.sleep(2)

# todo 2 click login with facebook
facebook_login = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')))
facebook_login.click()
print("facebook login button clicked.")

# wait until the facebook login page load.
time.sleep(2)

# important.change the window from main window to facebook load window.
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print("change to facebook window.")
print(driver.title)


facebook_email = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="email"]')))
facebook_email.send_keys(FACEBOOK_EMAIL)

# pretend to wait and then input password.
time.sleep(1)

facebook_password = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.NAME, "pass")))
facebook_password.send_keys(FACEBOOK_PASSWORD)

# pretend to wait and hit enter key.
time.sleep(1)

facebook_password.send_keys(Keys.ENTER)
print("login into facebook account.")

# wait the click card page load.
time.sleep(3)

# switch back to base window
driver.switch_to.window(base_window)
print(f"base window:\ntitle->{driver.title}\nname->{driver.window_handles}")

# todo 3 input email and password of facebook

# click allow location button
location_button = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')))
location_button.click()

# pretend to wait.
time.sleep(random.uniform(1, 2))

# click not allow notification anchor
not_allow_notification_anchor = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div/div[3]/button[2]/span')))
not_allow_notification_anchor.click()

# pretend to wait.
time.sleep(random.uniform(1, 2))

# click accept cookies button
accept_cookies_button = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/span')))
accept_cookies_button.click()

# wait the person card load.
time.sleep(5)


for n in range(DAILY_WIPE_TIMES):
    print(f"round {n}.")
    love_button = WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg')))
    love_button.click()
#     print(f"pick window:\ntitle->{driver.title}\nname->{driver.window_handles}")
#     time.sleep(random.uniform(1, 2))
#     try:
#         if n == 0:
#             heart_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg')
#
#         else:
#             heart_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button/span/span/svg')
#
#             heart_button.click()
#             print(n)
#             print("clicked like.")
#     # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
#     except NoSuchElementException:
#         time.sleep(random.uniform(2, 3))
#         print("do not find like button.")
#     except ElementClickInterceptedException:
#         try:
#             refuse_add_desk = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[2]/button[2]')
#             refuse_add_desk.click()
#             print("refuse add to desktop.")
#         except ElementClickInterceptedException:
#             # match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
#             match_popup = driver.find_element(By.XPATH, '//*[@id="o-1687095699"]/div/div/div[1]/div/div[4]/button/svg/path')
#             match_popup.click()
#             print("clicked match.")
#
# driver.quit()
