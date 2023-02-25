from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

def stergere_cont():
    baseUrl = "https://autoutil.thedemo.is/"
    driver = webdriver.Chrome()
    driver.get(baseUrl)
    driver.maximize_window()
    driver.implicitly_wait(15)
    time.sleep(3)

    # login
    intra_in_cont = driver.find_element(By.XPATH, "//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
    intra_in_cont.click()
    time.sleep(1)

    email = driver.find_element(By.XPATH, "//input[@type='text']")
    email.send_keys("carla_preda@yahoo.com")

    time.sleep(0.5)
    parola = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div[2]/input")
    parola.send_keys("Testare123@")

    intra_in_cont2 = driver.find_element(By.XPATH, "//div[@id='__next']//div[.='INTRĂ ÎN CONT']")
    intra_in_cont2.click()
    time.sleep(1)

    meniu = driver.find_elements(By.XPATH, "/html//div[@id='__next']//div/img").__getitem__(1)
    meniu.click()
    time.sleep(0.7)

    profilul_meu = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='Profilul meu']")
    profilul_meu.click()
    time.sleep(2)

    buton_stergere = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ȘTERGE CONTUL']")
    buton_stergere.click()
    time.sleep(2)

    buton_da = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='DA']")
    buton_da.click()
    time.sleep(2)