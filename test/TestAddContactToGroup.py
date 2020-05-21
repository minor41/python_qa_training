import random

from model.contact import Contact
from model.group import Group


def test_add_contact_to_group(app, db):
    if db.get_contact_list() == 0:
        app.contact.create_contact(Contact(first_name="test name", notes="hello world :)"))
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    old_group_with_contacts = db.get_contacts_in_group_list()
    contact_for_group = random.choice(contacts)
    group_for_contact = random.choice(groups)
    app.contact.add_contact_for_group(contact_for_group.contact_id, group_for_contact.group_id)
    new_group_with_contacts = db.get_contacts_in_group_list()
    # To Do !!!!!!!!!
    assert old_group_with_contacts == new_group_with_contacts




