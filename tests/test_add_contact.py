# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Michael", middlename="J.", lastname="Fox", nickname="Marti",
                               title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
                               mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
                               email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
                               notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
                               ayear=1985, path="C:\\img.jpg")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)