from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Slider():

    def test(self):
        baseUrl="https://jqueryui.com/slider/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)
        element=driver.find_element(By.XPATH,"//div[@id='slider']//span")
        time.sleep(2)

        try:
            actions=ActionChains(driver)
            actions.drag_and_drop_by_offset(element,100,0).perform() #orizontal-vertical
            time.sleep(3)
            print('sliding succesful')
            time.sleep(1)
        except:
            print("Sliding failed")



run_tests=Slider()
run_tests.test()
