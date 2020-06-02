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
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, mobile, work, "
                           "fax, homepage, notes, address2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, mobile, work, fax, homepage, notes,
                 address2) = row
                list_contact.append(Contact(contact_id=str(id), first_name=firstname, last_name=lastname,
                                            address=address, email=email, email2=email2, email3=email3,
                                            home_phone=home, mobile=mobile, work=work, fax=fax,
                                            homepage=homepage, notes=notes, address2=address2))
        finally:
            cursor.close()
        return list_contact

    def get_all_email_list(self):
        list_all_emails = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, email, email2, email3) = row
                list_all_emails.append(Contact(contact_id=str(id), email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list_all_emails

    def get_all_phone_list(self):
        list_all_emails = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, home, mobile, work, fax from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, home, mobile, work, fax) = row
                list_all_emails.append(Contact(contact_id=str(id), home_phone=home, mobile=mobile,
                                               work=work, fax=fax))
        finally:
            cursor.close()
        return list_all_emails

    def get_contacts_in_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, group_id from address_in_groups")
            for row in cursor:
                (id, group_id) = row
                list.append((Contact(contact_id=id), Group(group_id=group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()