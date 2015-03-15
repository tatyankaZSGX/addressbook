__author__ = 'ZSGX'


def test_delete_first_contact_from_homepage(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_from_homepage()
    app.session.logout()

def test_delete_first_contact_while_editing(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact_while_editing()
    app.session.logout()