__author__ = 'ZSGX'

from model.contact import Contact
import random

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


def test_edit_rand_contact_from_homepage(app, db, check_ui, data_contact):
    contact = data_contact
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    edcontact = random.choice(old_contacts)
    contact.id = edcontact.id
    app.contact.go_to_editpage_by_id_from_homepage(contact.id)
    app.contact.edit_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(edcontact)
    for atr in contact.__dict__:
        if contact.__dict__[atr] is not None:
            edcontact.__dict__[atr] = contact.__dict__[atr]
    old_contacts.append(edcontact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

def test_edit_rand_contact_from_details(app, db, check_ui, json_contact):
    contact = json_contact
    if len(db.get_contact_list()) == 0:
       app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    edcontact = random.choice(old_contacts)
    contact.id = edcontact.id
    app.contact.go_to_editpage_by_id_from_details(contact.id)
    app.contact.edit_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(edcontact)
    for atr in contact.__dict__:
        if contact.__dict__[atr] is not None:
            edcontact.__dict__[atr] = contact.__dict__[atr]
    old_contacts.append(edcontact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(app.contact.clean, db.get_contact_list()), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
