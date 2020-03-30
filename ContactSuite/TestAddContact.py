# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.personal_details(wd, first_name="Tester", middle_name="tes", last_name="Test", nickname="Bravo",
                              title="Mr.", homepage="www.test.com", notes="How are you ?")
        # wd.find_element_by_name("photo").click()

        self.company_details(wd, company="Big Test", address="Wherever")
        self.contact_numbers(wd, home="555111222", mobile="555222333", work="555333444", fax="555444555", home2="555555777")
        self.contact_emails(wd, email1="test1@test.test", email2="test2@test.test", email3="test3@test.test")
        self.birthday_date(wd, bday="10", bday_month="October", bday_year="1988")
        self.anniversary_date(wd, anniver_day="5", anniver_month="February", anniver_year="2021")
        self.group_selection(wd)
        self.home_address_details(wd, address2="Wherever2")
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def home_address_details(self, wd, address2):
        wd.find_element_by_name("address2").send_keys(address2)

    def group_selection(self, wd):
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def anniversary_date(self, wd, anniver_day, anniver_month, anniver_year):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(anniver_day)
        wd.find_element_by_xpath("(//option[@value='5'])[2]").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(anniver_month)
        wd.find_element_by_xpath("(//option[@value='February'])[2]").click()
        wd.find_element_by_name("ayear").send_keys(anniver_year)

    def birthday_date(self, wd, bday, bday_month, bday_year):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(bday)
        wd.find_element_by_xpath("//option[@value='10']").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(bday_month)
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").send_keys(bday_year)

    def contact_emails(self, wd, email1, email2, email3):
        wd.find_element_by_name("email").send_keys(email1)
        wd.find_element_by_name("email2").send_keys(email2)
        wd.find_element_by_name("email3").send_keys(email3)

    def contact_numbers(self, wd, home, mobile, work, fax, home2):
        wd.find_element_by_name("home").send_keys(home)
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("work").send_keys(work)
        wd.find_element_by_name("fax").send_keys(fax)
        wd.find_element_by_name("phone2").send_keys(home2)

    def company_details(self, wd, company, address):
        wd.find_element_by_name("company").send_keys(company)
        wd.find_element_by_name("address").send_keys(address)

    def personal_details(self, wd, first_name, middle_name, last_name, nickname, title, homepage, notes):
        wd.find_element_by_name("firstname").send_keys(first_name)
        wd.find_element_by_name("middlename").send_keys(middle_name)
        wd.find_element_by_name("lastname").send_keys(last_name)
        wd.find_element_by_name("nickname").send_keys(nickname)
        wd.find_element_by_name("title").send_keys(title)
        wd.find_element_by_name("homepage").send_keys(homepage)
        wd.find_element_by_name("notes").send_keys(notes)

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
