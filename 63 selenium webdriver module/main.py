import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_Path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_Path))

url = "https://www.amazon.com/kindle-the-lightest-and-most-compact-kindle/dp/B0B92489PD/ref=sr_1_4?crid=2ON6YW9OWU38N&keywords=kindle&qid=1668911373&sprefix=kindle%2Caps%2C302&sr=8-4"

# driver.get(url)
# price = driver.find_element(By.CLASS_NAME,"a-price")
# print(price.text)

# driver.get("https://www.python.org/")
# all_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# all_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# events = {}
#
# for n in range(len(all_dates)):
#     events[n] = {
#         "time" : all_dates[n].text,
#         "name" : all_name[n].text
#     }
# print(events)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com")
fname = driver.find_element(By.CLASS_NAME, "top")
fname.send_keys("Kritika")
lname = driver.find_element(By.CLASS_NAME,"middle")
lname.send_keys("Taank")
email = driver.find_element(By.CLASS_NAME, "bottom")
email.send_keys("viola.thebookaliciousmess@gmail.com")

final = driver.find_element(By.XPATH, "/html/body/form/button")
final.send_keys(Keys.ENTER)

time.sleep(10)