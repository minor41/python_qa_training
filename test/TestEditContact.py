from random import randrange

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact1 = Contact(first_name="Hello", middle_name="World", last_name="You", nickname="edit me", title="mr edit",
                       company_name="Big edit", address="edit")
    contact1.contact_id = old_contacts[index].contact_id
    app.contact.edit_contact_by_index(index, contact1)
    assert len(old_contacts) == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact1
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact_name(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
#     old_contacts = app.contact.get_contact_list()
#     contact1 = Contact(first_name="just first name", middle_name="just this", last_name="just last",)
#     app.contact.edit_first_contact(contact1)
# 
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact1
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
# 
# 
# def test_edit_contact_emails(app):
#     if app.contact.count_contact() == 0:
#         app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
#     old_contacts = app.contact.get_contact_list()
#     contact1 = Contact(email="just@test.edit", email2="email@just.com", email3="no 3rd email")
#     app.contact.edit_first_contact(contact1)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact1
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
