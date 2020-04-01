# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from ContactSuite.contact import Contact


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd, Contact(first_name="Tester", middle_name="tes", last_name="Test",
                                          nickname="Bravo", title="Mr.", company_name="Big Test",
                                          address="Wherever", homepage="www.test.com", home="555111222",
                                          mobile="555222333", work="555333444", fax="555444555",
                                          email1="test1@test.test", email2="test2@test.test",
                                          email3="test3@test.test", bday="10", bday_month="October",
                                          bday_year="1988", a_day="5", a_month="February", a_year="2021",
                                          home2="555555777", address2="Wherever2", notes="How are you ?"))
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_contact_with_basic_info(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.contact_creation(wd, Contact(first_name="Tessa12", middle_name="", last_name="Test456",
                                          nickname="", title="", company_name="Big MO",
                                          address="", homepage="www.345.com", home="",
                                          mobile="555222333", work="555333444", fax="",
                                          email1="test1@test.test", email2="",
                                          email3="", bday="", bday_month="-",
                                          bday_year="", a_day="", a_month="-", a_year="",
                                          home2="", address2="", notes=""))
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def contact_creation(self, wd, contact_details):
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact_details.first_name)
        wd.find_element_by_name("middlename").send_keys(contact_details.middle_name)
        wd.find_element_by_name("lastname").send_keys(contact_details.last_name)
        wd.find_element_by_name("nickname").send_keys(contact_details.nickname)
        wd.find_element_by_name("title").send_keys(contact_details.title)
        wd.find_element_by_name("company").send_keys(contact_details.company_name)
        wd.find_element_by_name("address").send_keys(contact_details.address)
        wd.find_element_by_name("home").send_keys(contact_details.home)
        wd.find_element_by_name("mobile").send_keys(contact_details.mobile)
        wd.find_element_by_name("work").send_keys(contact_details.work)
        wd.find_element_by_name("fax").send_keys(contact_details.fax)
        wd.find_element_by_name("email").send_keys(contact_details.email1)
        wd.find_element_by_name("email2").send_keys(contact_details.email2)
        wd.find_element_by_name("email3").send_keys(contact_details.email3)
        wd.find_element_by_name("homepage").send_keys(contact_details.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_details.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_details.bday_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(contact_details.bday_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_details.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_details.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(contact_details.a_year)
        wd.find_element_by_xpath("//option[@value='[none]']").click()
        wd.find_element_by_name("address2").send_keys(contact_details.address2)
        wd.find_element_by_name("phone2").send_keys(contact_details.home2)
        wd.find_element_by_name("notes").send_keys(contact_details.notes)

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
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
