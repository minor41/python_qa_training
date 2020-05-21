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
    group_for_contact = random.randrange(len(groups))
    app.contact.add_contact_for_group(contact_for_group.contact_id, group_for_contact)
    new_group_with_contacts = db.get_contacts_in_group_list()
    assert sorted(old_group_with_contacts, key=Group.id_or_max) == sorted(new_group_with_contacts, key=Group.id_or_max)




