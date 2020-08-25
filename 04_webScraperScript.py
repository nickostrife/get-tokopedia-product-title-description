#! python3
# Script to demonstrate tokopedia web scraping: get product name & product description.

import requests, time, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Download chrome webdriver and specify its path (https://chromedriver.chromium.org/downloads)
driver = webdriver.Chrome('C:\chromedriver.exe')

url = 'https://www.tokopedia.com/victory-trend/jepitan-gantungan-sepatu-jepitan-anti-angin-hhd-272'

try:
    # Load page and idle for 1 sec.
    driver.get(url)
    time.sleep(1)

    # Hit PAGE DOWN key to let dynamic content loads, and let it idle for 5 secs.
    driver.find_element_by_css_selector('html').send_keys(Keys.PAGE_DOWN)
    time.sleep(5)

    # Capture the page source.
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    # Find <script> tag, the data is in list[1], and pass it as json format
    scripts = soup.find_all('script', type='application/ld+json')[1].string
    data = json.loads(scripts)

    # Print data
    print('title: {}'.format(data['name']))
    print('description: {}'.format(data['description']))

finally:
    driver.quit()