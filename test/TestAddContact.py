# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="Tester23", middle_name="tes", last_name="Test",
                      nickname="Bravo", title="Mr.", company_name="Big Test",
                      address="Wherever", homepage="www.test.com", home="555111222",
                      mobile="555222333", work="555333444", fax="555444555",
                      email="test1@test.test", email2="test2@test.test",
                      email3="test3@test.test", bday="10", bmonth="October",
                      byear="1988", aday="5", amonth="February", ayear="2021",
                      phone2="555555777", address2="Wherever2", notes="How are you ?")
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_contact_with_basic_info(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(first_name="Trick", middle_name="", last_name="Truck",
#                       nickname="", title="", company_name="Big MO",
#                       address="", homepage="www.345.com", home="",
#                       mobile="555222333", work="", fax="",
#                       email="test1@test.test", email2="",
#                       email3="", bday="", bmonth="-",
#                       byear="", aday="", amonth="-", ayear="",
#                       phone2="", address2="", notes="")
#     app.contact.create_contact(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
