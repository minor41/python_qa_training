import jsonpickle
import os
import random
import string
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day(prefix):
    days = ["", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    return random.choice(days)


def random_year(prefix):
    return str(random.randint(1900, 2020))


def random_month(prefix):
    months = ["-", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December", ]
    return random.choice(months)


testdata = [Contact(first_name="", middle_name="", last_name="", nickname="", title="", company_name="",
                    address="", home_phone="", mobile="", work="", fax="", email="", email2="", email3="",
                    homepage="", bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", phone2="",
                    address2="", notes="")] + \
            [Contact(random_string("first_name", 10), random_string("middle_name", 10), random_string("last_name", 20),
                     random_string("nickname", 10), random_string("title", 5), random_string("company_name", 20),
                     random_string("address", 20),random_string("home_phone", 10), random_string("mobile", 10),
                     random_string("work", 10), random_string("fax", 10), random_string("email", 10),
                     random_string("email2", 10), random_string("email3", 10), random_string("homepage", 10),
                     random_day("bday"), random_month("bmonth"), random_year("byear"),
                     random_day("aday"), random_month("amonth"), random_year("ayear"),
                     random_string("phone2", 10), random_string("address2", 10), random_string("notes", 10), )
             for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
