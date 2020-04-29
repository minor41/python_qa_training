import re
from model.contact import Contact


def test_random_contact_on_home_page(app):
    if app.contact.count_contact() == 0:
        contact = Contact(first_name="Trick", middle_name="", last_name="Truck",
                          nickname="", title="", company_name="Big MO",
                          address="", homepage="www.345.com", home_phone="",
                          mobile="555222333", work="", fax="",
                          email="test1@test.test", email2="",
                          email3="", bday="", bmonth="-",
                          byear="", aday="", amonth="-", ayear="",
                          phone2="", address2="", notes="")
        app.contact.create_contact(contact)
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.first_name == contact_from_edit_page.first_name
    assert contact_from_homepage.last_name == contact_from_edit_page.last_name
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_emails_from_home_page == merge_emails_like_on_edit_page(contact_from_edit_page)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_edit_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile, contact.work, contact.phone2]))))
