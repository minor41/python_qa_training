from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def edit_first_contact(self, contact_details):
        wd = self.app.wd
        # select first contact to edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact form
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact_details.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact_details.middle_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact_details.last_name)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact_details.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact_details.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact_details.company_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact_details.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact_details.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact_details.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact_details.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact_details.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact_details.email1)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact_details.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact_details.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact_details.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact_details.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact_details.bday_month)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact_details.bday_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact_details.a_day)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact_details.a_month)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact_details.a_year)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact_details.address2)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact_details.home2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact_details.notes)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def create_contact(self, contact_details):
        wd = self.app.wd
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
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()