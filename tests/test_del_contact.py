__author__ = 'ZSGX'
from model.contact import Contact

def test_delete_first_contact_from_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_from_homepage()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts == new_contacts

def test_delete_first_contact_while_editing(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact_while_editing()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1]=[]
    assert old_contacts == new_contacts