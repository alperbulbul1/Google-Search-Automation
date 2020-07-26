from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

page = 5

browser = webdriver.Firefox()
search_term = str(input("What are you looking for? "))
browser.get("http://www.google.com/")

search = browser.find_elements_by_name("q")
search[0].send_keys(search_term)
search[0].send_keys(Keys.ENTER)

total = []
while True:
    page != 0

    time.sleep(1)

    i = browser.find_element_by_id("rso")
    for j in i.find_elements_by_class_name("g"):
        for k in j.find_elements_by_tag_name("h3"):
            print(k.text)
        url = j.find_element_by_tag_name("a")
        print(url.get_attribute("href"))
        print()
        new = ((k.text,url.get_attribute("href")))
        total.append(new)
    browser.find_element_by_xpath('//*[@id="pnnext"]').click()
    page = page -1
    if page == 0:
        break

df = pd.DataFrame(total, columns=["Title","Url"])

df.to_csv(f"{search_term}-Google.csv",index=False)

browser.close()
