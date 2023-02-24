from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date,timedelta

StartDate = "March 1, 2023"
end_date = StartDate + timedelta(days=31)
end_date=end_date.strftime("%B")
print(end_date)