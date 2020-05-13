from model.contact import Contact
from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(group_id=group.group_id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_con_list = app.contact.get_contact_list()

    def clean(contact):
        return Contact(contact_id=contact.contact_id, first_name=contact.first_name,
                       last_name=contact.last_name.strip())
    db_con_list = map(clean, db.get_contact_list())
    assert sorted(ui_con_list, key=Contact.id_or_max) == sorted(db_con_list, key=Contact.id_or_max)