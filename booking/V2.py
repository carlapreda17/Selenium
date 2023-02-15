from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Booking():

    def test(self):
        baseUrl = "https://www.booking.com/index.html?aid=2253598&label=_63eb9325eeaab1034342fcac"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        textToSelect="Singapore"

        driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        location=driver.find_element(By.XPATH,"//input[@id='ss']")
        location.send_keys("Sin")

        liElements=driver.find_elements(By.XPATH,"//li[@role='option']")
        time.sleep(4)

        for element in liElements:
           if textToSelect in element.text:
               element.click()
               break

        time.sleep(6)



run_tests=Booking()
run_tests.test()