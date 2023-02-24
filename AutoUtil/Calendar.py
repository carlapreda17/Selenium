from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date


class Calendar():

    def test(self):
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)

        #login
        intra_in_cont = driver.find_element(By.XPATH, "//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
        intra_in_cont.click()
        time.sleep(1)

        email = driver.find_element(By.XPATH, "//input[@type='text']")
        email.send_keys("carla_preda@yahoo.com")

        time.sleep(0.5)
        parola = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div[2]/input")
        parola.send_keys("Testare123@")

        intra_in_cont2 = driver.find_element(By.XPATH, "//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
        intra_in_cont2.click()
        time.sleep(1)

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

        itp = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div/div[3]/div[.='adaugă alertă']")
        itp.click()
        time.sleep(0.7)





run_tests=Calendar()
run_tests.test()