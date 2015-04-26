__author__ = 'ZSGX'

from model.contact import Contact
import re

def test_match_db_contact_with_homepage(app, db):
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = [app.contact.clean(el) for el in db.get_contact_list()]
    for contact in contacts_from_db:
        contact.tel = merge_tel_like_homepage(contact)
        contact.mails = merge_mail_like_homepage(contact)
    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(contacts_from_db, key=Contact.id_or_max)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_tel_like_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                        map(lambda x: clear(x),
                            filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,contact.workphone, contact.phone2]))))

def merge_mail_like_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                                filter(lambda x: x is not None,[contact.email, contact.email2,contact.email3])))