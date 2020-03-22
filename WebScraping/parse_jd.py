"""

This is a temporary script file.
"""
import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver

CSV_File = "urls_jd.csv"

options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')
options.add_argument("--disable-notifications")

urls = []


def scroll_to_bottom():
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def find_urls():
    """
    find all urls and save in a list
    """
    try:
        soup = BeautifulSoup(page_source, 'html.parser')
        list_items = soup.find_all("li", {"class": "cntanr"})
        for item in list_items:
            if item.has_attr('data-href'):
                urls.append({item['data-href']})
        print("URL length: {}".format(len(urls)))
        next_anchor = soup.find("a", {"rel": "next"}, href=True)
        return next_anchor['href'] if next_anchor and next_anchor.has_attr('href') else None
    except Exception as e:
        print("Error while parsing soup: {}".format(e))
    return None


def write_to_file():
    global urls
    if urls:
        with open(CSV_File, 'a', newline='') as result_file:
            wr = csv.writer(result_file, dialect='excel')
            wr.writerows(urls)
        urls = []


if __name__ == "__main__":
    start_url = "https://www.justdial.com/Indore/Doctors-ENT-Surgeons/nct-10941619"

    # create a new Chrome session
    driver = webdriver.Chrome(chrome_options=options)
    driver.implicitly_wait(30)
    while start_url:
        driver.get(start_url)
        SCROLL_PAUSE_TIME = 0.5
        scroll_to_bottom()
        page_source = driver.page_source
        start_url = find_urls()

        if len(urls) > 200:
            # write_to_file()
            break

    write_to_file()
