from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class GenericSs():

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
        self.TakeSs(driver)

    def TakeSs(self,driver):
         """
         Takes screenshot of the current open web page
         :param driver
         :return:
         """
         fileName=str(round(time.time()*1000))+".png"
         screenDirectory="/Users/40737/ss-uri"
         destinationFile=screenDirectory+fileName
         try:
             driver.save_screenshot(destinationFile)
             print("Screenshot saved")
         except NotADirectoryError:
             print("Not a directory issue")




run_tests=GenericSs()
run_tests.test()