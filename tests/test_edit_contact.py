__author__ = 'ZSGX'

from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="new", middlename="Jasd", lastname="Foxsa", nickname="Madsti",
                               title="adasor", company="Hoasdadood", address="Ladngeles")
    old_contacts = app.contact.get_contact_list()
    contact.id = old_contacts[0].id
    app.contact.go_to_editpage_from_homepage()
    app.contact.edit_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_edit_first_contact_from_details(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(firstname="test"))
#    app.contact.go_to_editpage_from_details()
#   app.contact.edit_contact(Contact(firstname="", middlename="J.", lastname="Fox", nickname="Marti",
#                              title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
#                              mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
#                              email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
#                              notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
#                              ayear=1985, path="C:\\img.jpg"))
