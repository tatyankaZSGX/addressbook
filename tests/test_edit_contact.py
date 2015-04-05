__author__ = 'ZSGX'

from model.contact import Contact
from random import randrange
import random
import string
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="Michael", middlename="J.", lastname="Fox", nickname="Marti",
                    title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
                    mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
                    email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
                    notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
                    ayear=1985, path="C:\\img.jpg")] + [
    Contact(firstname=random_string("", 10), middlename=random_string("", 10), lastname=random_string("", 10),
            nickname=random_string("", 10), title=random_string("", 10), company=random_string("", 10),
            address=random_string("", 10), homephone=random_string("", 10), mobilephone=random_string("", 10),
            workphone=random_string("", 10), fax=random_string("", 10), email2=random_string("", 10),
            email3=random_string("", 10), homepage=random_string("", 10), address2=random_string("", 10),
            phone2=random_string("", 10), notes=random_string("", 100), bday=9, bmonth=6, byear=1961, aday=26,
            amonth=10, ayear=1985, path="C:\\img.jpg")
    for i in range(2)]


def test_edit_first_contact_from_homepage(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="first", middlename="Jasd", lastname="homepage", nickname="Madsti",
                               title="adasor", company="Hoasdadood", address="Ladngeles")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.go_to_editpage_from_homepage(0)
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_edit_first_contact_from_details(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="first", middlename="Jasd", lastname="editing", nickname="Madsti",
                               title="adasor", company="Hoasdadood", address="Ladngeles")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.go_to_editpage_from_details(0)
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_edit_rand_contact_from_homepage(app, contact):
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

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_edit_rand_contact_from_details(app, contact):
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
