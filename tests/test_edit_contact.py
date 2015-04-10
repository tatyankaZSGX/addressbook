__author__ = 'ZSGX'

from model.contact import Contact
from random import randrange

#def test_edit_first_contact_from_homepage(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test"))
#    contact = Contact(firstname="first", middlename="Jasd", lastname="homepage", nickname="Madsti",
#                               title="adasor", company="Hoasdadood", address="Ladngeles")
#    old_contacts = app.contact.get_contact_list()
#    contact.id = old_contacts[0].id
#    app.contact.go_to_editpage_from_homepage(0)
#    app.contact.edit_contact(contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_first_contact_from_details(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(firstname="test"))
#    contact = Contact(firstname="first", middlename="Jasd", lastname="editing", nickname="Madsti",
#                               title="adasor", company="Hoasdadood", address="Ladngeles")
#    old_contacts = app.contact.get_contact_list()
#    contact.id = old_contacts[0].id
#    app.contact.go_to_editpage_from_details(0)
#    app.contact.edit_contact(contact)
#    assert len(old_contacts) == app.contact.count()
#    new_contacts = app.contact.get_contact_list()
#    old_contacts[0] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_rand_contact_from_homepage(app, data_contact):
    contact = data_contact
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.go_to_editpage_from_homepage(index)
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_rand_contact_from_details(app, data_contact):
    contact = data_contact
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.go_to_editpage_from_details(index)
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
