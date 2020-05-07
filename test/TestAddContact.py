# -*- coding: utf-8 -*-
import pytest
from data.add_contact import constant as test_data_contact
from model.contact import Contact


@pytest.mark.parametrize("contact", test_data_contact, ids=[repr(x) for x in test_data_contact])
def test_add_contact(app, contact):
    # pass
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

