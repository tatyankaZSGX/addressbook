__author__ = 'ZSGX'
from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="mod_name", header="mod_header", footer="mod_footer"))
    app.session.logout()
