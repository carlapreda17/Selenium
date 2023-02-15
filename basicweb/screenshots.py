from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl="https://courses.letskodeit.com/"
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.find_element(By.XPATH,"//a[normalize-space()='Sign In']").click()
        driver.find_element(By.ID,"email").send_keys("abc@yahoo.com")
        driver.find_element(By.ID,"password").send_keys("abd")
        time.sleep(5)

        driver.find_element(By.ID,"login").click()

        destinationFileName="/Users/40737/ss-uri.png"

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved")
        except NotADirectoryError:
            print("Not a directory issue")



run_tests=Screenshots()
run_tests.test()