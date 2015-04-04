__author__ = 'ZSGX'

import re
from random import randrange

def test_match_contact_with_homepage(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_props_from_editpage(index)
    assert contact_from_homepage.tel == merge_tel_like_homepage(contact_from_editpage)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_tel_like_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.phone2]))))

