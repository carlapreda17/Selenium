from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByIdName():
    def test(self):
        baseURL="https://courses.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByXPath=driver.find_element(By.XPATH,"/html//input[@id='displayed-text']")
        if elementByXPath is not None:
            print("Element found by XPATH")
        else:
            print("oh no")

        elementByCSS=driver.find_element(By.CSS_SELECTOR,"input#displayed-text")
        if elementByCSS is not None:
            print("Element found by CSS")

run_tests=FindByIdName()
run_tests.test()