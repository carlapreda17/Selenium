from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class JS():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get(baseUrl) este la fel cu comanda de mai jos
        driver.execute_script("window.location='https://courses.letskodeit.com/practice';")
        driver.implicitly_wait(5)

        #element=driver.find_element(By.ID,"name")
        element=driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

        time.sleep(4)

run_tests=JS()
run_tests.test()
