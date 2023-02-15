from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragAndDrop():

    def test(self):
        baseUrl="https://jqueryui.com/droppable/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)
        fromElement=driver.find_element(By.ID,"draggable")
        toElement=driver.find_element(By.ID,"droppable")
        time.sleep(2)

        try:
            actions=ActionChains(driver)
            #actions.drag_and_drop(fromElement,toElement).perform()
            actions.click_and_hold(fromElement).move_to_element(toElement).perform()

            print("Drag And Drop Element Succesful")
            time.sleep(2)
        except:
            print("Drag and drop failed")



run_tests=DragAndDrop()
run_tests.test()
