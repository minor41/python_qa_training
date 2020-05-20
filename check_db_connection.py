from fixture.db import DbFixture
# from fixture.orm import ORMFixture


# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
from model.group import Group

db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")


# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()


try:
    contacts = db.get_contacts_in_group_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()

# try:
#     l = db.get_contacts_not_in_group(Group(group_id='228'))
#     for item in l:
#         print(item)
#     print(len(l))
# finally:
#     pass # db.destroy()
