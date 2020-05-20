from model.contact import Contact


def test_contact_list(app, db):
    ui_con_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(contact_id=contact.contact_id, first_name=contact.first_name,
                       last_name=contact.last_name.strip(), address=contact.address,
                       all_emails_from_home_page=contact.all_emails_from_home_page,
                       all_phones_from_home_page=contact.all_phones_from_home_page)
    db_con_list = map(clean, db.get_contact_list())
    assert sorted(ui_con_list, key=Contact.id_or_max) == sorted(db_con_list, key=Contact.id_or_max)