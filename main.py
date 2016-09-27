from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Create a new instance of the Chrome driver
driver = webdriver.Chrome('C:\chromedriver\chromedriver.exe')

# go to the google home page
driver.get("http://www.torn.com")

#Login1
time.sleep(random.uniform(3,5))

username1 = driver.find_element_by_id("player")
username1.send_keys("EMAIL")

password1 = driver.find_element_by_id("password")
password1.send_keys("PASSWORD")
password1.submit()
time.sleep(random.uniform(3,5))

#Deposit money1
driver.get("http://www.torn.com/properties.php#/p=options&tab=vault")
#vault = driver.find_element_by_id("icon32").click()
time.sleep(random.uniform(3,5))

#Scroll down to bottom of page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

vaultsubmit1 = driver.find_element_by_xpath('//*[@id="properties-page-wrap"]/div[3]/div[8]/div[3]/form[2]/div[2]/span/span/input')
vaultsubmit1.click()

time.sleep(random.uniform(3,5))
#Do Gym
""" gym1 = driver.find_element_by_xpath('//*[@id="nav-gym"]/a').click()
recaptchaA = driver.find_element_by_xpath('//*[@id="ui-id-2"]/span').click()
recaptchaB = driver.find_element_by_xpath('//*[@id="recaptcha-anchor"]/div[5]').click()
"""

#Logout1
logout1 = driver.find_element_by_class_name("logout").click()
time.sleep(random.uniform(3,5))

driver.quit()
