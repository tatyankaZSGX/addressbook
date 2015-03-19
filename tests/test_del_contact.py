__author__ = 'ZSGX'
from model.contact import Contact

def test_delete_first_contact_from_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact_from_homepage()

def test_delete_first_contact_while_editing(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.delete_first_contact_while_editing()