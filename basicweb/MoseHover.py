from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MouseHover():

    def test(self):
        baseUrl="https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(2)

        element=driver.find_element(By.ID,"mousehover")

        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"
        time.sleep(2)

        try:
            actions=ActionChains(driver)
            actions.move_to_element(element).perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            TopLink = driver.find_element(By.XPATH, itemToClickLocator)
            #TopLink.click()
            actions.move_to_element(TopLink).click().perform()
            print("Item cliked")
        except:
            print('no')


run_tests=MouseHover()
run_tests.test()
