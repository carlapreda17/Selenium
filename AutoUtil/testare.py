from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date

baseUrl = "https://autoutil.thedemo.is/acasa/autovehicul/606/alerte/2/adauga"
driver = webdriver.Chrome()
driver.get(baseUrl)
driver.maximize_window()
driver.implicitly_wait(15)
time.sleep(3)