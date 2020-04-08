from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="edit", middle_name="edit", last_name="edit",
                                           nickname="edit me", title="mr edit", company_name="Big edit",
                                           address="edit", homepage="", home="",
                                           mobile="", work="", fax="",
                                           email1="test1@test.edit", email2="",
                                           email3="", bday="-", bday_month="-",
                                           bday_year="", a_day="-", a_month="-", a_year="",
                                           home2="", address2="", notes="we edit all"))
    app.session.logout()
