# download the chrome driver from here
# https://sites.google.com/a/chromium.org/chromedriver/downloads

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import glob

# The PATH to the chromedriver you downloaded
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# The location of the folder in goolge drive 
driver.get("https://drive.google.com/drive/folders/xxxxxxxxxxxxxxxxxxxxxxx")

list_of_files = glob.glob("folder path location on the os")

search = driver.find_element_by_name("identifier")
search.send_keys("your email address")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(4)
search = driver.find_element_by_name("password")
search.send_keys("your password")
time.sleep(3)
search.send_keys(Keys.RETURN)
time.sleep(5)

for file in list_of_files:
    webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys("u").perform()
    time.sleep(2)
    pyautogui.write(file)
    time.sleep(1)
    pyautogui.press('enter')
