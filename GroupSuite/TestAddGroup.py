# -*- coding: utf-8 -*-
import pytest
from GroupSuite.application_group import ApplicationGroup
from GroupSuite.group import Group


@pytest.fixture()
def app(request):
    fixture = ApplicationGroup()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="test 123", header="test 123", footer="test 123"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()

