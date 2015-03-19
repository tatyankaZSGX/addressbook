__author__ = 'ZSGX'


def test_delete_first_contact_from_homepage(app):
    app.contact.delete_first_contact_from_homepage()

def test_delete_first_contact_while_editing(app):
    app.contact.delete_first_contact_while_editing()