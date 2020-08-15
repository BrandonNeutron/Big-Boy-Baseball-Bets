from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pytz
from datetime import datetime
import csv
import sys
import math
import random


def login(driver):
    driver.get("https://www.fangraphs.com/dailyprojections.aspx?pos=all&stats=bat&type=sabersim&team=0&lg=all&players=0")
    time.sleep(2)

    tg = driver.find_elements_by_xpath("//table[@class='rgMasterTable']/tbody/tr/td")
    for i in tg:
        print(i.text)
def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome = "C:/Users/blh16/Downloads/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome, options=chrome_options)
    login(driver)
    print("asdf")
main()