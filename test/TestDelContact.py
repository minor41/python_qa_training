from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    app.contact.delete_first_contact()
