import mysql.connector
from model.contact import Contact
from model.group import Group


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list_group = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (group_id, name, header, footer) = row
                list_group.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_group

    def get_contact_list(self):
        list_contact = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname) = row
                list_contact.append(Contact(contact_id=str(id), first_name=firstname, middle_name=middlename,
                                            last_name=lastname))
        finally:
            cursor.close()
        return list_contact

    def destroy(self):
        self.connection.close()