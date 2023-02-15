from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Iframe():

    def test(self):
        baseUrl = "https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0,1000);")

        #Switch Frame using Id
        driver.switch_to.frame("courses-iframe")
        # Switch Frame using name
        #driver.switch_to.frame("iframe-name")
        # Switch Frame using numbers
        # driver.switch_to.frame(0)
        time.sleep(3)
        #Search Course
        searchBox = driver.find_element(By.XPATH, "//input[@id='search']")
        searchBox.send_keys("python")
        time.sleep(3)

        #Switch back to default frame
        driver.switch_to.default_content()

        driver.execute_script("window.scrollBy(0,-1000);")
        driver.find_element(By.ID, "name").send_keys("Test Successful")
        time.sleep(3)

ff = Iframe()
ff.test()