from datetime import datetime
from pony.orm import *
from model.contact import Contact
from model.group import Group


class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        group_id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        contact_id = PrimaryKey(int, column='id')
        first_name = Optional(str, column='firstname')
        last_name = Optional(str, column='lastname')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)

    def __init__(self,  host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_modal(self, groups):
        def convert(group):
            return Group(group_id=str(group.group_id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_modal(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_modal(self, contacts):
        def convert(contact):
            return Contact(contact_id=str(contact.contact_id), first_name=contact.first_name, last_name=contact.last_name)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_modal(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = self.select_from_db(group)
        return self.convert_contacts_to_modal(orm_group.contacts)

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = self.select_from_db(group)
        return self.convert_contacts_to_modal(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))

    def select_from_db(self, group):
        return list(select(g for g in ORMFixture.ORMGroup if g.group_id == group.group_id))[0]
