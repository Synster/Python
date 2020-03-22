"""

This is a temporary script file.
"""
import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver


if __name__ == "__main__":
    start_url = "https://www.sulekha.com/indore"
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    driver.get(start_url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    menus = soup.find_all("div", {"class" :"stabs-panel"})

    i = 0
    for menu in menus:
        categories = []
        i = i+1
        elements = menu.find_all("a")
        for element in elements:
            if element.has_attr('href') and element.has_attr('title'):
                categories.append((element['title'], element['href']))

        if categories:
            with open("menu-{0}.csv".format(i), 'w',  newline='') as result_file:
                wr = csv.writer(result_file, dialect='excel')
                wr.writerows(categories)
    driver.quit()



