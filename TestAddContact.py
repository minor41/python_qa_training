# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.personal_details(wd)
        # wd.find_element_by_name("photo").click()

        self.company_details(wd)
        self.contact_numbers(wd)
        self.contact_emails(wd)
        self.birthday_date(wd)
        self.anniversary_date(wd)
        self.group_selection(wd)
        self.home_address_details(wd)
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def home_address_details(self, wd):
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").send_keys("Wherever2")

    def group_selection(self, wd):
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def anniversary_date(self, wd):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("5")
        wd.find_element_by_xpath("(//option[@value='5'])[2]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_xpath("(//option[@value='February'])[2]").click()
        wd.find_element_by_name("ayear").send_keys("2021")

    def birthday_date(self, wd):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("10")
        wd.find_element_by_xpath("//option[@value='10']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").send_keys("1988")

    def contact_emails(self, wd):
        wd.find_element_by_name("email").send_keys("test1@test.test")
        wd.find_element_by_name("email2").send_keys("test2@test.test")
        wd.find_element_by_name("email3").send_keys("test3@test.test")

    def contact_numbers(self, wd):
        wd.find_element_by_name("home").send_keys("555111222")
        wd.find_element_by_name("mobile").send_keys("555222333")
        wd.find_element_by_name("work").send_keys("555333444")
        wd.find_element_by_name("fax").send_keys("555444555")
        wd.find_element_by_name("phone2").send_keys("555555777")

    def company_details(self, wd):
        wd.find_element_by_name("company").send_keys("Big Test")
        wd.find_element_by_name("address").send_keys("Wherever")

    def personal_details(self, wd):
        wd.find_element_by_name("firstname").send_keys("Tester")
        wd.find_element_by_name("middlename").send_keys("tes")
        wd.find_element_by_name("lastname").send_keys("Test")
        wd.find_element_by_name("nickname").send_keys("Bravo")
        wd.find_element_by_name("title").send_keys("Mr.")
        wd.find_element_by_name("homepage").send_keys("www.test.com")
        wd.find_element_by_name("notes").send_keys("How are you ?")

    def init_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit_contact_creation(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
