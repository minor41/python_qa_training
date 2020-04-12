from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    app.contact.edit_first_contact(Contact(first_name="edit", middle_name="edit", last_name="edit",
                                           nickname="edit me", title="mr edit", company_name="Big edit",
                                           address="edit", homepage="", home="",
                                           mobile="", work="", fax="",
                                           email="test1@test.edit", email2="",
                                           email3="", bday="-", bmonth="-",
                                           byear="", aday="-", amonth="-", ayear="",
                                           phone2="", address2="", notes="we edit all"))


def test_edit_contact_name(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    app.contact.edit_first_contact(Contact(first_name="just first name", middle_name="just this",
                                           last_name="just last",))


def test_edit_contact_emails(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    app.contact.edit_first_contact(Contact(email="just@test.edit", email2="email@just.com", email3="no 3rd email"))
