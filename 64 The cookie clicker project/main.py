import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://orteil.dashnet.org/experiments/cookie/"
chrome_driver_Path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_Path))

driver.get(url)

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + (60*5)

while True:
     cookie.click()

     if time.time() > timeout:
         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
         item_prices = []

         for price in all_prices:
             element_text = price.text
             if element_text != '':
                 const = int(element_text.split("-")[1].strip().replace(",",""))
                 item_prices.append(const)

         cookie_upgrade = {}
         for n in range(len(item_prices)):
             cookie_upgrade[item_prices[n]] = item_ids[n]

         money_element = driver.find_element(By.CSS_SELECTOR, "moni").text
         if "," in money_element:
             money_element = money_element.replace(",", "")
         cookie_count = money_element

         affordable_upgrades = {}
         for cost, id in cookie_upgrade.items():
             if int(cookie_count) > cost:
                 affordable_upgrades[cost] = id

         highest_price_affordable_upgrade = max(affordable_upgrades)
         print(highest_price_affordable_upgrade)

         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

         driver.find_element(By.ID, f"#{to_purchase_id}").click()

         timeout = time.time() + 5

     if time.time() > five_min:
         cookie_per_s = driver.find_element(By.ID, "#cps").text
         print(cookie_per_s)
         break

time.sleep(five_min*2)