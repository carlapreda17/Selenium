from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date,timedelta


end_date = date.today() + timedelta(days=6)
end_date=end_date.strftime('%d')
print(end_date[1])