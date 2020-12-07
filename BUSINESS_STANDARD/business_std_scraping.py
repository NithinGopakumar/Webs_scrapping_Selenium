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
from tqdm import tqdm
import pandas as pd

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--incognito')
# set webdriver path here it may vary
path = r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\chromedriver.exe"
driver = webdriver.Chrome(path , options=chrome_option)


url = 'https://www.business-standard.com/'
driver.get(url)
print(driver.title)
driver.implicitly_wait(10)

markets = driver.find_element_by_link_text('MARKETS')
markets.click()
driver.implicitly_wait(5)


first_block = driver.find_element_by_xpath('//*[@class="btm-section"]')
print(first_block)
driver.implicitly_wait(10)

posts = first_block.find_elements_by_tag_name('h2')
print(len(posts))

listoflinks = []
for post in posts:
    a_tag = post.find_element_by_tag_name('a').get_property('href')
    if (a_tag == 'https://www.business-standard.com/article/markets/market-live-markets-sensex-nifty-bse-nse-sgx-nifty-tcs-wipro-covid-120100800159_1.html'):
        continue
    listoflinks.append(a_tag)

print(listoflinks)
print(len(listoflinks))

top_stories = driver.find_element_by_xpath('//*[@class="coutent-panel bs-new-top-story-listing-block"]')
print(top_stories)
driver.implicitly_wait(10)

articles = top_stories.find_elements_by_tag_name('a')
print(len(articles))

# listoflinks = []
for i in range(len(articles)):
    article = articles[i]
    ppp = article.get_property('href')
    # if (ppp == 'https://economictimes.indiatimes.com/markets/stocks/recos'):
    #     continue
    listoflinks.append(ppp)

print("The final list of links is: {}".format(listoflinks))
print(len(listoflinks))

# final = []
# for i in tqdm(listoflinks):
#     driver.get(i)
#     driver.implicitly_wait(5)
#     # description = 0
#     description = driver.find_element_by_xpath('//*[@class="p-content"]')
#
#     if True:
#         # description = driver.find_element_by_xpath('//*[@class="p-content"]').text
#         print(description.text)
#     else:
#         continue

final = []
for i in tqdm(listoflinks):
    driver.get(i)
    driver.implicitly_wait(5)
    try:
        title = driver.find_element_by_xpath('//*[@class="headline"]').text
        description = driver.find_element_by_xpath('//*[@class="p-content"]').text
        print(title)
        print(description)
        temp = {'TITLE': title,
                'TEXT': description,
                'LINKS': i}
        final.append(temp)
    except:
        continue


df = pd.DataFrame(final)
print(df)
df.to_csv(r'C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\business_std_scrapped.csv')
driver.quit()