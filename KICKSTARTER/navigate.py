from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from datetime import datetime
import time
from time import strftime

# set webdriver path here it may vary
path = r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\chromedriver.exe"
driver = webdriver.Chrome(path)

url = 'https://www.kickstarter.com/'
driver.get(url)
print(driver.title)

# search = browser.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "js-search-term-gs", " " ))]')
# search.click()
# search.send_keys('machine learning')
# search.send_keys(Keys.RETURN)

link = driver.find_element_by_link_text("Design & Tech")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Explore Design"))
    )
    element.click()
    driver.back()
    driver.back()
except:
    driver.quit()