from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByTagClass():
    def test(self):
        baseURL="https://courses.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByTag=driver.find_element(By.TAG_NAME,"a")
        if elementByTag is not None:
            print("Element found by Tag")
        else:
            print("oh no")

        elementByClass=driver.find_element(By.CLASS_NAME,"inputs")
        if elementByClass is not None:
            print("Element found by Class")

run_tests=FindByTagClass()
run_tests.test()