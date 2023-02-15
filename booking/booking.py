from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class calendarSelections():

    def test(self):
        baseUrl = "https://www.booking.com/index.html?aid=2253598&label=_63eb9325eeaab1034342fcac"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        textToSelect = "Singapore"

        driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
        driver.find_element(By.XPATH,"//div[contains(@data-mode,'checkin')]//span[@class='sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb']").click()

        time.sleep(5)

        driver.find_element(By.XPATH,"//span[contains(@aria-label,'16 februarie 2023')]//span[contains(@aria-hidden,'true')][normalize-space()='16']").click()
        driver.find_element(By.XPATH,"//span[@aria-label='2 martie 2023']//span[@aria-hidden='true'][normalize-space()='2']").click()
        changeMonth=driver.find_element(By.XPATH,"//td[contains(@class,'bui-calendar__date bui-calendar__date--selected')]")
        changeMonth.click()

        location = driver.find_element(By.XPATH, "//input[@id='ss']")
        location.send_keys("Sin")

        liElements = driver.find_elements(By.XPATH, "//li[@role='option']")
        time.sleep(4)

        for element in liElements:
            if textToSelect in element.text:
                element.click()
                break

        time.sleep(5)



        search = driver.find_element(By.XPATH, "//span[contains(@class,'b-button__text')]")
        search.click()

        time.sleep(6)


run_tests=calendarSelections()
run_tests.test()