from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact_edit):
        wd = self.app.wd
        # select first contact to edit
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact_edit)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None
        WebDriverWait(wd, 10).until(ec.visibility_of_element_located((By.ID, "search_count")))

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # select random contact
        wd.find_elements_by_name("selected[]")[index].click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()
        self.contact_cache = None
        WebDriverWait(wd, 10).until(ec.visibility_of_element_located((By.ID, "search_count")))

    def create_contact(self, contact_details):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact_details)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None
        WebDriverWait(wd, 10).until(ec.visibility_of_element_located((By.ID, "search_count")))

    def fill_contact_form(self, contact_details):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact_details.first_name)
        self.change_contact_field_value("middlename", contact_details.middle_name)
        self.change_contact_field_value("lastname", contact_details.last_name)
        self.change_contact_field_value("nickname", contact_details.nickname)
        self.change_contact_field_value("title", contact_details.title)
        self.change_contact_field_value("company", contact_details.company_name)
        self.change_contact_field_value("address", contact_details.address)
        self.change_contact_field_value("home", contact_details.home)
        self.change_contact_field_value("mobile", contact_details.mobile)
        self.change_contact_field_value("work", contact_details.work)
        self.change_contact_field_value("fax", contact_details.fax)
        self.change_contact_field_value("email", contact_details.email)
        self.change_contact_field_value("email2", contact_details.email2)
        self.change_contact_field_value("email3", contact_details.email3)
        self.change_contact_field_value("homepage", contact_details.homepage)
        self.select_value_from_list("bday", contact_details.bday)
        self.select_value_from_list("bmonth", contact_details.bmonth)
        self.change_contact_field_value("byear", contact_details.byear)
        self.select_value_from_list("aday", contact_details.aday)
        self.select_value_from_list("amonth", contact_details.amonth)
        self.change_contact_field_value("ayear", contact_details.ayear)
        self.selecting_group()
        self.change_contact_field_value("address2", contact_details.address2)
        self.change_contact_field_value("phone2", contact_details.phone2)
        self.change_contact_field_value("notes", contact_details.notes)

    def select_value_from_list(self, position, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(position).click()
            Select(wd.find_element_by_name(position)).select_by_visible_text(value)

    def selecting_group(self):
        wd = self.app.wd
        try:
            wd.find_element_by_xpath("//option[@value='[none]']").click()
        except NoSuchElementException:
            return False
        return True

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        # if not wd.current_url.endswith("/index.php"):
        wd.find_element_by_link_text("home").click()

    def count_contact(self):
        wd = self.app.wd
        # self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                first_name = element.find_elements_by_css_selector('td')[2].text
                last_name = element.find_elements_by_css_selector('td')[1].text
                contact_id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(first_name=first_name, last_name=last_name, contact_id=contact_id))
        return list(self.contact_cache)

