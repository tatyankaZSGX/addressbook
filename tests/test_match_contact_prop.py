__author__ = 'ZSGX'

from model.contact import Contact

def test_match_db_contact_with_homepage(app, db):
    contacts_from_homepage = app.contact.get_contact_list()
    assert sorted(contacts_from_homepage, key=Contact.id_or_max) == sorted(db.get_contact_list(), key=Contact.id_or_max)
