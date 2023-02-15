import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChService

class RunChromeTests():
    def test(self):
        chserivce=ChService(executable_path="C:\\Pyhton\\pythonProject\\Selenium\\drivers\\chromedriver.exe")

        driver=webdriver.Chrome(service=chserivce)

        driver.get("https://courses.letskodeit.com/practice")
        time.sleep(5)


run_tests=RunChromeTests()
run_tests.test()