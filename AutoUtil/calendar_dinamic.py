from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from datetime import date

class Calendar():

    def test(self):
        baseUrl = "https://autoutil.thedemo.is/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.maximize_window()
        driver.implicitly_wait(15)
        time.sleep(3)

        #login
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

        # adauga masina
        adauga = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[@role='button']")
        adauga.click()
        time.sleep(1)

        nr_inmatriculare = driver.find_element(By.XPATH, "/html//div[@id='__next']//input")
        nr_inmatriculare.send_keys("VN 06 HRK")
        time.sleep(1)

        adauga_masina = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='ADAUGĂ MAȘINĂ']")
        adauga_masina.click()
        time.sleep(1)

        itp = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[3]/div/div[3]/div[.='adaugă alertă']")
        itp.click()
        time.sleep(0.7)

        today = date.today()
        luna = today.strftime("%B")
        zi = today.strftime("%d")


        if luna=="February":
            if int(zi)+2<28:
                zi_noua=int(zi)+2
                print(zi_noua)
                data_itp = driver.find_element(By.XPATH, "/html//div[@id='choice-calendar']//div[.='"+ str(zi_noua) +"']")
                data_itp.click()
                time.sleep(0.2)
                if int(zi)+6>28:
                    slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]").click()
                    zi_noua = int(zi)+6-28
                    time.sleep(2)
                    data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(zi_noua) + "']").click()
                    time.sleep(1)

                    zi_noua=int(zi)+16-28
                    data_itp = driver.find_element(By.XPATH, "/html//div[@id='choice-calendar']//div[.='" + str(zi_noua) + "']").click()
                    time.sleep(1)
                    print("succes")

                    zi_noua=int(zi)+31-28
                    print(zi_noua)
                    if zi_noua>31:
                        slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]").click()
                        zi_noua=zi_noua-31;
                        data_itp = driver.find_element(By.XPATH, "/html//div[@id='choice-calendar']//div[.='" + str(zi_noua) + "']").click()
                        time.sleep(1)
                    else:
                        slider = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[@role='slider']/div[1]/div[3]").click()
                        data_itp = driver.find_element(By.XPATH, "/html//div[@id='choice-calendar']//div[.='" + str(zi_noua) + "']").click()
                        time.sleep(3)
                        ziua_1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']").click()
                        ziua_5 =driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='5 zile']").click()
                        ziua_15 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='15 zile']").click()
                        ziua_30 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='30 zile']").click()
                        time.sleep(3)
                        sms = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[1]/label/div[2]/div/div[2]/div").click()
                        time.sleep(0.2)

                        email2 = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[3]/label/div[2]/div/div[2]").click()
                        time.sleep(0.2)

                        adaugare_alerta = driver.find_elements(By.XPATH,"/html//div[@id='__next']//div[@role='button']").__getitem__(-1)
                        adaugare_alerta.click()
                        time.sleep(1)

                        ok = driver.find_element(By.XPATH,"/html//div[@id='__next']/div/div[2]/div[2]//div[@role='dialog']//div[@role='button']").click()
                        time.sleep(10)

                        confirmare = driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='CONTINUĂ']").click()
                        time.sleep(2)

                        adaugare_alerta.click()
                        time.sleep(2)


            if int(zi)+2>28:
                    zi_noua=int(zi)+2-28
                    print
                    data_itp=driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[5]//div[.='"+ str(zi_noua) +"']")
                    data_itp.click()
                    time.sleep(3)
                    print("succes")
                    ziua_1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']")
                    ziua_1.click()
                    time.sleep(0.2)

            if int(zi)+6<28:
                    zi_noua=int(zi)+6
                    data_itp = driver.find_element(By.XPATH,"/html//div[@id='choice-calendar']//div[.='" + str(zi_noua) + "']")
                    data_itp.click()
                    print("succes")
                    ziua_1 = driver.find_element(By.XPATH, "/html//div[@id='__next']//div[.='1 zi']").click()
                    time.sleep(2)
                    ziua_5=driver.find_element(By.XPATH,"/html//div[@id='__next']//div[.='5 zile']").click()
                    time.sleep(2)








run_tests=Calendar()
run_tests.test()