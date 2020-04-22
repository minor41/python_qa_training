from model.group import Group


def test_edit_first_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    old_groups = app.group.get_group_list()
    group1 = Group(name="edit name", header="edit header", footer="edit footer")
    group1.group_id = old_groups[0].group_id
    app.group.edit_first_group(group1)
    assert len(old_groups) == app.group.count_group()
    new_groups = app.group.get_group_list()
    old_groups[0] = group1
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


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
