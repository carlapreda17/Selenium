from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Size():

    def test(self):
        baseUrl="https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        height=driver.execute_script("return window.innerHeight;")
        width=driver.execute_script("return window.innerWidth;")
        print("Height: "+str(height))
        print("Width: " +str(width))

run_tests=Size()
run_tests.test()