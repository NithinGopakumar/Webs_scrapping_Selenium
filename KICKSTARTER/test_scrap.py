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

# set webdriver path here it may vary
path = r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\chromedriver.exe"
driver = webdriver.Chrome(path)

url = 'https://www.kickstarter.com/'
driver.get(url)
print(driver.title)
time.sleep(3)

link = driver.find_element_by_link_text("Design & Tech")
link.click()
time.sleep(3)


link1 = driver.find_element_by_link_text("Explore Technology")
link1.click()
time.sleep(3)

projects = driver.find_elements_by_class_name("js-track-project-card")
# print(projects[0])
#
# ppp = projects[0]
#
# print(ppp.find_element_by_tag_name('a').get_property('href'))

listoflinks = []
for proj in projects:
    ppp = proj.find_element_by_tag_name('a')
    listoflinks.append(ppp.get_property('href'))

print(listoflinks)

final = []
for i in tqdm(listoflinks):
    driver.get(i)
    time.sleep(5)

    title = driver.find_element_by_xpath('//*[@id="react-project-header"]/div/div/div[2]/div/div[2]/div/h2').text
    description = driver.find_element_by_xpath('//*[@id="react-campaign"]/section/div/div/div/div[1]/div/div/div[2]').text

    ###If every description is to be appended to a single txt file.....
    # textfile = open(r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\textfile.txt", "a" , encoding="utf-8")

    ###If every description is to be saved onto separate txt files....
    Index = listoflinks.index(i)
    textfile = open(r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\textfile_{}.txt".format(Index), "w" , encoding="utf-8")
    textfile.write(description)

    temp = {'TITLE':title,
            'TEXT':description,
            'LINKS':i}
    final.append(temp)

# final = []
# for j in range(len(listoflinks)):
#     for i in tqdm(listoflinks):
#         driver.get(i)
#         time.sleep(5)
#         description = driver.find_element_by_xpath(
#             '//*[@id="react-campaign"]/section/div/div/div/div[1]/div/div/div[2]').text
#
#         textfile = open(r"C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\textfile_{}.txt".format(j), "w" , encoding="utf-8")
#         textfile.write(description)
#         temp = {'TEXT':description,
#             'LINKS':i}
#         final.append(temp)

df = pd.DataFrame(final)
print(df)
df.to_csv(r'C:\Users\nithi\PycharmProjects\NEW_latest\Aarna_Python_Basics\scrapped.csv')
driver.quit()