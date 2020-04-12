# -*- coding: utf-8 -*-
from time import sleep

from model.group import Group


def test_add_group(app):
    app.group.create_group(Group(name="test 123", header="test 123", footer="test 123"))


def test_add_empty_group(app):
    app.group.create_group(Group(name="", header="", footer=""))

