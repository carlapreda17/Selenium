from selenium import webdriver
from selenium.webdriver.common.by import By

class FindByList():
    def test(self):
        baseURL="https://courses.letskodeit.com/practice"
        driver=webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementByTag=driver.find_elements(By.TAG_NAME,"a")
        length2=len(elementByTag)
        if elementByTag is not None:
            print("Size of the list is: " + str(length2))
        else:
            print("oh no")

        elementByClass=driver.find_elements(By.CLASS_NAME,"inputs")
        length=len(elementByClass)
        if elementByClass is not None:
            print("Size of the list is: " + str(length))

run_test=FindByList()
run_test.test()