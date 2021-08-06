# download the chrome driver from here
# https://sites.google.com/a/chromium.org/chromedriver/downloads


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
import glob

PATH = "path to the driver file" + "\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("driver folder URL path")

search = driver.find_element_by_name("identifier")
search.send_keys("your email address")
search.send_keys(Keys.RETURN)
driver.implicitly_wait(4)
search = driver.find_element_by_name("password")
search.send_keys("your password")
time.sleep(3)
search.send_keys(Keys.RETURN)
time.sleep(5)

list_of_files = glob.glob("your directory path" + "\\*")
list1 = []
for file in list_of_files:
    list1.append(file + "\n")

#create a txt file for the program and it will check if the files is uploaded allready or not 
f = open('the path of the txt file', "r+")
list2 = []
for line in f:
    list2.append(line)
list_of_unuploaded_files = [x for x in list1 if not x in list2]

if len(list_of_unuploaded_files) == 0:
    print("no new files to upload")
else:
    for file in list_of_unuploaded_files:
        webdriver.ActionChains(driver).key_down(Keys.SHIFT).send_keys("u").perform()
        time.sleep(2)
        pyautogui.write(file)
        time.sleep(1)
        pyautogui.press('enter')
        f.write(file)

f.close()
driver.close()
