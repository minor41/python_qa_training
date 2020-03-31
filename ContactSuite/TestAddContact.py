# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from ContactSuite.personal import PersonalDetails
from ContactSuite.company import CompanyDetails
from ContactSuite.numbers import ContactNumbers
from ContactSuite.emails import ContactEmails
from ContactSuite.birthday_date import Birthday
from ContactSuite.anniversary_date import Anniversary


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.personal_details(wd, PersonalDetails(first_name="Tester", middle_name="tes", last_name="Test",
                                                  nickname="Bravo", title="Mr.", homepage="www.test.com",
                                                  address2="Wherever2", notes="How are you ?"))
        self.company_details(wd, CompanyDetails(company_name="Big Test", address="Wherever"))
        self.contact_numbers(wd, ContactNumbers(home="555111222", mobile="555222333", work="555333444", fax="555444555",
                             home2="555555777"))
        self.contact_emails(wd, ContactEmails(email1="test1@test.test", email2="test2@test.test",
                                              email3="test3@test.test"))
        self.birthday_date(wd, Birthday(bday="10", bday_month="October", bday_year="1988"))
        self.anniversary_date(wd, Anniversary(a_day="5", a_month="February", a_year="2021"))
        self.group_selection(wd)
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_contact_with_basic_info(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_contact_creation(wd)
        self.personal_details(wd, PersonalDetails(first_name="Tester123", middle_name="", last_name="Test321",
                                                  nickname="Gamma", title="", homepage="",
                                                  address2="", notes=""))
        self.company_details(wd, CompanyDetails(company_name="", address=""))
        self.contact_numbers(wd, ContactNumbers(home="", mobile="555222333", work="555333444", fax="",
                             home2=""))
        self.contact_emails(wd, ContactEmails(email1="test1@test.test", email2="",
                                              email3=""))
        self.birthday_date(wd, Birthday(bday="", bday_month="-", bday_year=""))
        self.anniversary_date(wd, Anniversary(a_day="", a_month="-", a_year=""))
        self.group_selection(wd)
        self.submit_contact_creation(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def group_selection(self, wd):
        wd.find_element_by_xpath("//option[@value='[none]']").click()

    def anniversary_date(self, wd, anniversary_date):
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(anniversary_date.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(anniversary_date.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").send_keys(anniversary_date.a_year)

    def birthday_date(self, wd, birthday_date):
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(birthday_date.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(birthday_date.bday_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").send_keys(birthday_date.bday_year)

    def contact_emails(self, wd, emails):
        wd.find_element_by_name("email").send_keys(emails.email1)
        wd.find_element_by_name("email2").send_keys(emails.email2)
        wd.find_element_by_name("email3").send_keys(emails.email3)

    def contact_numbers(self, wd, numbers):
        wd.find_element_by_name("home").send_keys(numbers.home)
        wd.find_element_by_name("mobile").send_keys(numbers.mobile)
        wd.find_element_by_name("work").send_keys(numbers.work)
        wd.find_element_by_name("fax").send_keys(numbers.fax)
        wd.find_element_by_name("phone2").send_keys(numbers.home2)

    def company_details(self, wd, company):
        wd.find_element_by_name("company").send_keys(company.company_name)
        wd.find_element_by_name("address").send_keys(company.address)

    def personal_details(self, wd, personal):
        wd.find_element_by_name("firstname").send_keys(personal.first_name)
        wd.find_element_by_name("middlename").send_keys(personal.middle_name)
        wd.find_element_by_name("lastname").send_keys(personal.last_name)
        wd.find_element_by_name("nickname").send_keys(personal.nickname)
        wd.find_element_by_name("title").send_keys(personal.title)
        wd.find_element_by_name("homepage").send_keys(personal.homepage)
        wd.find_element_by_name("notes").send_keys(personal.notes)
        wd.find_element_by_name("address2").send_keys(personal.address2)

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
