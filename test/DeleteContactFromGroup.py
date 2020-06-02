import random
from model.contact import Contact
from model.group import Group


def test_delete_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    contacts = db.get_contact_list()
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    groups = db.get_group_list()
    group_for_contact = random.choice(groups)
    contact_for_group = random.choice(contacts)
    old_contacts_in_groups = db.get_contacts_in_group_list()
    app.contact.delete_contact_from_group(contact_for_group.contact_id, group_for_contact.group_id)
    new_contacts_in_groups = db.get_contacts_in_group_list()
    assert len(old_contacts_in_groups) - 1 == len(new_contacts_in_groups)
