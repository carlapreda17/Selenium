from selenium import webdriver

class BrowserInteractions():
    def test(self):
        driver=webdriver.Chrome()
        baseUrl="https://courses.letskodeit.com/practice"

        #Window Maximize
        driver.maximize_window()

        #Open Url
        driver.get(baseUrl)

        #getTitle
        title=driver.title
        print("title is: " + title)

        #get current Url
        url=driver.current_url
        print("Current Url of the web page is: " + url)

        #Browser Refresh
        driver.refresh()
        print("Browser referesh 1st time")

        #Open Url
        driver.get("https://courses.letskodeit.com/register")

        #Driver Back
        driver.back()
        print("Back")

        #Driver Forward
        driver.forward()
        print("one step forward")

        #Get the page source
        page=driver.page_source

        #Browser Close
        driver.close()

run_tests=BrowserInteractions()
run_tests.test()