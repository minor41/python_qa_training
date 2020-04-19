# -*- coding: utf-8 -*-
from time import sleep

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="test 123", header="test 123", footer="test 123"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_group(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

