import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_Path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_Path))
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3356277069&f_AL=true&f_WT=2&geoId=102713980&keywords=python%20intern&location=India&refresh=true&sortBy=R")

ACCOUNT_EMAIL = "taank.kritika@gmail.com"
ACCOUNT_PASSWORD = "weneedslides"
PHONE = 8595031393

sign_in_button = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button" )
submit_button.click()