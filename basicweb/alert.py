from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Alert():

    def test(self):

        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver.get(baseUrl) este la fel cu comanda de mai jos
        driver.execute_script("window.location='https://courses.letskodeit.com/practice';")
        driver.implicitly_wait(5)

        driver.find_element(By.ID,"name").send_keys("Carla")
        time.sleep(2)
        driver.find_element(By.ID,"alertbtn").click()
        time.sleep(2)
        alert1=driver.switch_to.alert
        alert1.accept()
        time.sleep(2)
        driver.find_element(By.ID,"confirmbtn").click()
        time.sleep(2)
        alert2=driver.switch_to.alert
        alert2.dismiss()



run_tests=Alert()
run_tests.test()
