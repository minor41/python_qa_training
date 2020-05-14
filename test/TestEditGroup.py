from random import randrange
from model.group import Group
import random


def test_edit_first_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create_group(Group(name="test"))
    old_groups = db.get_group_list()
    group_to_edit = random.choice(old_groups)
    # index = randrange(len(old_groups))
    edit_data = Group(name="edit name", header="edit header", footer="edit footer")
    # edit_data.group_id = group_to_edit.group_id
    app.group.edit_group_by_id(group_to_edit.group_id, edit_data)
    new_groups = db.get_group_list()
    # assert len(old_groups) == app.group.count_group()
    # old_groups[group_to_edit.group_id] = edit_data
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_name(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_group() == 0:
#         app.group.create_group(Group(name="test"))
#     app.group.edit_first_group(Group(name="edit just name"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count_group() == 0:
#         app.group.create_group(Group(name="test"))
#     app.group.edit_first_group(Group(header="edit just header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
