from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from AutoUtil.login import login


def adauga():

        baseUrl = "https://autoutil.thedemo.is/acasa"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)
        login()

        # adauga masina
        adauga = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[@role='button']")
        adauga.click()
        time.sleep(1)

        nr_inmatriculare = driver.find_element(By.XPATH, "/html//div[@id='__next']//input")
        nr_inmatriculare.send_keys("VN 06 HRK")
        time.sleep(1)

        adauga_masina = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ADAUGĂ MAȘINĂ']")
        adauga_masina.click()
        time.sleep(1)

adauga()