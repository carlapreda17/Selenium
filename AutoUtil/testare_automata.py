from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class AutoUtil():

    def inregistrare(self):
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get(baseUrl)


        #creeaza contul
        inregistrare=driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[.='CREEAZĂ CONT']").__getitem__(-1)
        inregistrare.click()

        email=driver.find_element(By.XPATH,"//input[@type='text']")
        email.send_keys("carla_preda@yahoo.com")

        time.sleep(0.5)
        parola=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/div[2]/input")
        parola.send_keys("Testare123@")

        confirmare_parola=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[5]/div[2]/input")
        confirmare_parola.send_keys("Testare123@")
        time.sleep(0.5)

        continua=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[@role='button']//div[@class='css-1dbjc4n']")
        continua.click()
        time.sleep(2)

        nume=driver.find_elements(By.XPATH,"/html//div[@id='__next']//input").__getitem__(-4)
        nume.send_keys("Carla")
        time.sleep(1)

        telefon = driver.find_elements(By.XPATH,"/html//div[@id='__next']//input").__getitem__(-3)
        telefon.send_keys("0737528681")
        time.sleep(2)

        buton1=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[2]/div/div[2]/div")
        buton1.click()

        buton2=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/div[2]/label")
        buton2.click()

        creeaza_cont=driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']/div").__getitem__(-1)
        creeaza_cont.click()
        time.sleep(4)


    def login_alerte(self):
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(5)
        time.sleep(3)

        #login
        intra_in_cont=driver.find_element(By.XPATH,"//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
        intra_in_cont.click()
        time.sleep(2)

        email = driver.find_element(By.XPATH, "//input[@type='text']")
        email.send_keys("carla_preda@yahoo.com")

        time.sleep(1)
        parola = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div[2]/input")
        parola.send_keys("Testare123@")

        intra_in_cont2 = driver.find_element(By.XPATH,"//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
        intra_in_cont2.click()
        time.sleep(2)

        # adauga masina
        adauga = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[@role='button']")
        adauga.click()
        time.sleep(2)

        nr_inmatriculare = driver.find_element(By.XPATH, "/html//div[@id='__next']//input")
        nr_inmatriculare.send_keys("VN 06 HRK")
        time.sleep(2)

        adauga_masina = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ADAUGĂ MAȘINĂ']")
        adauga_masina.click()
        time.sleep(2)

        #alerte


        itp = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div/div[3]/div[.='adaugă alertă']")
        itp.click()
        time.sleep(0.7)

        data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='24']")
        data_itp.click()
        time.sleep(0.4)

        ziua1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
        sms = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div")
        email2 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]")
        adaugare_alerta = driver.find_elements(By.XPATH, "/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
        ziua_1.click()
        time.sleep(0.4)
        sms.click()
        time.sleep(0.5)
        email2.click()
        time.sleep(0.5)
        adaugare_alerta.click()
        time.sleep(3)

        ok = driver.find_element(By.XPATH,"/html//div[@id='__next']/div/div[2]/div[2]//div[@role='dialog']//div[@role='button']")
        ok.click()
        time.sleep(10)

        confirmare = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='CONTINUĂ']")
        confirmare.click()
        time.sleep(5)

        adaugare_alerta.click()
        time.sleep(3)

        rca=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[5]/div/div[3]/div[.='adaugă alertă']")
        rca.click()
        time.sleep(1)

        data_rca = driver.find_element(By.XPATH, "/html//div[@id='choice-calendar']//div[.='28']")
        data_rca.click()
        time.sleep(0.4)

        anunt1.click()
        sms.click()
        email2.click()
        adaugare_alerta.click()
        time.sleep(3)



run_tests=AutoUtil()
run_tests.login_alerte()