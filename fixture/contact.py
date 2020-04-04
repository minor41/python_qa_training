class ContactHelper:

    def __init__(self, app):
        self.app = app

    def contact(self, contact_details):
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