# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PetclinicDemo2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:9999"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test01_add_user_moham(self):
        driver = self.driver
        # Label: Add User: Moham
        # ERROR: Caught exception [ERROR: Unsupported command [resizeWindow | 1913,992 | ]]
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.LINK_TEXT,"Add Owner").click()
        driver.find_element(By.ID,"firstName").click()
        driver.find_element(By.ID,"firstName").clear()
        driver.find_element(By.ID,"firstName").send_keys("Robin")
        driver.find_element(By.ID,"lastName").clear()
        driver.find_element(By.ID,"lastName").send_keys("Mohan")
        driver.find_element(By.ID,"address").clear()
        driver.find_element(By.ID,"address").send_keys("Pr. Catharina-Amaliastraat 5")
        driver.find_element(By.ID,"city").clear()
        driver.find_element(By.ID,"city").send_keys("The Hague")
        driver.find_element(By.ID,"telephone").clear()
        driver.find_element(By.ID,"telephone").send_keys("0634336608")
        driver.find_element(By.ID,"lastName").click()
        driver.find_element(By.ID,"lastName").clear()
        driver.find_element(By.ID,"lastName").send_keys("Moham")
        driver.find_element(By.CSS_SELECTOR,"div.container.xd-container").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()

    # Label: Find User: Moham
    def test02_check_user_moham(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Moham")
        driver.find_element(By.CSS_SELECTOR,"div.col-sm-offset-2.col-sm-10").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        assert driver.find_element(By.CSS_SELECTOR,"strong").text == 'Robin Moham'

        # Label: Add User: van Oranje
    def test03_add_user_van_oranje(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.CSS_SELECTOR,"a[title=\"find owners\"]").click()
        driver.find_element(By.LINK_TEXT,"Add Owner").click()
        driver.find_element(By.ID,"firstName").click()
        driver.find_element(By.ID,"firstName").clear()
        driver.find_element(By.ID,"firstName").send_keys("Wimlex")
        driver.find_element(By.ID,"lastName").clear()
        driver.find_element(By.ID,"lastName").send_keys("van Oranje")
        driver.find_element(By.ID,"address").clear()
        driver.find_element(By.ID,"address").send_keys("Paleis Noordeinde")
        driver.find_element(By.ID,"city").clear()
        driver.find_element(By.ID,"city").send_keys("Den Haag")
        driver.find_element(By.ID,"telephone").clear()
        driver.find_element(By.ID,"telephone").send_keys("1234567890")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()

        # Label: Find User: Oranje
    def test04_check_user_van_oranje(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.CSS_SELECTOR,"a[title=\"find owners\"]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Oranje")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("van Oranje")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        assert driver.find_element(By.CSS_SELECTOR,"strong").text == 'Wimlex van Oranje'

        # Label: Update User: Moham -> Mohan
    def test05_update_user_moham(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.CSS_SELECTOR,"a[title=\"find owners\"]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Moham")
        driver.find_element(By.CSS_SELECTOR,"div.col-sm-offset-2.col-sm-10").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        driver.find_element(By.LINK_TEXT,"Edit Owner").click()
        driver.find_element(By.ID,"lastName").click()
        driver.find_element(By.ID,"lastName").clear()
        driver.find_element(By.ID,"lastName").send_keys("Mohan")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()

        # Label: Find User: Moham
    def test06_check_user_moham(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Moham")
        driver.find_element(By.CSS_SELECTOR,"div.col-sm-offset-2.col-sm-10").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        assert driver.find_element(By.ID,"owner.errors")

        # Label: Find User: Mohan
    def test07_check_user_mohan(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Mohan")
        driver.find_element(By.ID,"search-owner-form").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        assert driver.find_element(By.CSS_SELECTOR,"strong").text == 'Robin Mohan'

        # Label: Add pet to Mohan
    def test08_add_pet_mushi_to_mohan(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Mohan")
        driver.find_element(By.CSS_SELECTOR,"div.col-sm-offset-2.col-sm-10").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        driver.find_element(By.LINK_TEXT,"Add New Pet").click()
        driver.find_element(By.ID,"name").click()
        driver.find_element(By.ID,"name").clear()
        driver.find_element(By.ID,"name").send_keys("Mushi")
        driver.find_element(By.ID,"birthDate").click()
        driver.find_element(By.LINK_TEXT,"10").click()
        Select(driver.find_element(By.ID,"type")).select_by_visible_text("cat")
        driver.find_element(By.CSS_SELECTOR,"option[value=\"cat\"]").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()

        # Label: Add pet to van Oranje
    def test09_add_pet_vicky_to_van_oranje(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.ID,"search-owner-form").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("van Oranje")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        driver.find_element(By.LINK_TEXT,"Add New Pet").click()
        driver.find_element(By.ID,"name").click()
        driver.find_element(By.ID,"name").clear()
        driver.find_element(By.ID,"name").send_keys("Vicky")
        driver.find_element(By.ID,"birthDate").click()
        driver.find_element(By.LINK_TEXT,"8").click()
        Select(driver.find_element(By.ID,"type")).select_by_visible_text("dog")
        driver.find_element(By.CSS_SELECTOR,"option[value=\"dog\"]").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()

        # Label: check pet Mohan
    def test10_check_pet_mushi_in_mohan(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.CSS_SELECTOR,"a[title=\"find owners\"]").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("Mohan")
        driver.find_element(By.CSS_SELECTOR,"div.col-sm-offset-2.col-sm-10").click()
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        print()
        assert driver.find_element(By.CSS_SELECTOR,"dd").text == "Mushi"
        assert driver.find_element(By.XPATH,"//dd[2]").text == "2022-02-10"
        assert driver.find_element(By.XPATH,"//dd[3]").text == "cat"
    
     # Label: check mushi not in wimlex
    def test11_pet_mushi_not_in_van_oranje(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element(By.XPATH,"//div[@id='main-navbar']/ul/li[2]/a/span[2]").click()
        driver.find_element(By.ID,"search-owner-form").click()
        driver.find_element(By.NAME,"lastName").click()
        driver.find_element(By.NAME,"lastName").clear()
        driver.find_element(By.NAME,"lastName").send_keys("van Oranje")
        driver.find_element(By.CSS_SELECTOR,"button.btn.btn-default").click()
        assert driver.find_element(By.CSS_SELECTOR,"dd").text != "Mushi"
        assert driver.find_element(By.XPATH,"//dd[2]").text != "2022-01-10"
        assert driver.find_element(By.XPATH,"//dd[3]").text != "cat"
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()