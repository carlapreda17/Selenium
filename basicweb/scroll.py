from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class Scroll():

    def test(self):
        baseUrl="https://courses.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)

        #Scroll Down
        driver.execute_script("window.scrollBy(0,600);")
        time.sleep(4)

        #Scroll Up
        driver.execute_script("window.scrollBy(0,-600);")
        time.sleep(4)

        #Scroll Elem into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        #Native way to scroll element into view
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -600);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))
        driver.execute_script("window.scrollBy(0, -150);")


run_tests=Scroll()
run_tests.test()