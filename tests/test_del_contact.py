__author__ = 'ZSGX'
from model.contact import Contact
import random

#def test_delete_first_contact_from_homepage(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_first_contact_from_homepage()
#    assert len(old_contacts) - 1 == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[0:1]=[]
#    assert old_contacts == new_contacts

#def test_delete_first_contact_while_editing(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.delete_first_contact_while_editing()
#    assert len(old_contacts) - 1 == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[0:1]=[]
#    assert old_contacts == new_contacts

def test_delete_rand_contact_from_homepage(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_from_homepage(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.contact.clean, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_delete_rand_contact_while_editing(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id_from_homepage(contact.id)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(app.contact.clean, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)