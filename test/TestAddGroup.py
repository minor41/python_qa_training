# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group1 = Group(name="test 123", header="test 123", footer="test 123")
    app.group.create_group(group1)
    assert len(old_groups) + 1 == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups.append(group1)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group2 = Group(name="ttt", header="", footer="")
#     app.group.create_group(group2)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group2)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

