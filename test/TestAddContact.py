# -*- coding: utf-8 -*-
import pytest
from fixture.application_contact import ApplicationContact
from model.contact import Contact


@pytest.fixture()
def app(request):
    fixture = ApplicationContact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact_creation(Contact(first_name="Tester", middle_name="tes", last_name="Test",
                                 nickname="Bravo", title="Mr.", company_name="Big Test",
                                 address="Wherever", homepage="www.test.com", home="555111222",
                                 mobile="555222333", work="555333444", fax="555444555",
                                 email1="test1@test.test", email2="test2@test.test",
                                 email3="test3@test.test", bday="10", bday_month="October",
                                 bday_year="1988", a_day="5", a_month="February", a_year="2021",
                                 home2="555555777", address2="Wherever2", notes="How are you ?"))
    app.session.logout()


def test_add_contact_with_basic_info(app):
    app.session.login(username="admin", password="secret")
    app.contact_creation(Contact(first_name="Tessa12", middle_name="", last_name="Test456",
                                 nickname="", title="", company_name="Big MO",
                                 address="", homepage="www.345.com", home="",
                                 mobile="555222333", work="555333444", fax="",
                                 email1="test1@test.test", email2="",
                                 email3="", bday="", bday_month="-",
                                 bday_year="", a_day="", a_month="-", a_year="",
                                 home2="", address2="", notes=""))
    app.session.logout()

