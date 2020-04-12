from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="edit name", header="edit header", footer="edit footer"))


def test_edit_group_name(app):
    app.group.edit_first_group(Group(name="edit just name"))


def test_edit_group_header(app):
    app.group.edit_first_group(Group(header="edit just header"))
