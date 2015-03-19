__author__ = 'ZSGX'

from model.contact import Contact

def test_edit_first_contact(app):
    app.contact.go_to_editpage_from_homepage()
    app.contact.edit_contact(Contact(firstname="new", middlename="Jasd", lastname="Foxsa", nickname="Madsti",
                               title="adasor", company="Hoasdadood", address="Ladngeles"))

def test_edit_first_contact_from_details(app):
    app.contact.go_to_editpage_from_details()
    app.contact.edit_contact(Contact(firstname="", middlename="J.", lastname="Fox", nickname="Marti",
                               title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
                               mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
                               email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
                               notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
                               ayear=1985, path="C:\\img.jpg"))
