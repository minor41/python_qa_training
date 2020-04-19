from model.group import Group


def test_edit_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="edit name", header="edit header", footer="edit footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="edit just name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_edit_group_header(app):
    old_groups = app.group.get_group_list()
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(header="edit just header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
