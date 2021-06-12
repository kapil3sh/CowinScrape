from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "D:\Cowin\CowinScrape\driver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.cowin.gov.in/")

pin = driver.find_element_by_id("mat-tab-label-0-1")
pin.click()

search = driver.find_element_by_id("mat-input-0")
search.send_keys("400018")

search_btn = driver.find_element_by_class_name("pin-search-btn")
search_btn.send_keys(Keys.RETURN)

table = driver.find_element_by_class_name("center-name-text")
print(table.text)


