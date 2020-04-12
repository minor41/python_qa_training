from model.group import Group


def test_edit_first_group(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="edit name", header="edit header", footer="edit footer"))


def test_edit_group_name(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(name="edit just name"))


def test_edit_group_header(app):
    if app.group.count_group() == 0:
        app.group.create_group(Group(name="test"))
    app.group.edit_first_group(Group(header="edit just header"))
