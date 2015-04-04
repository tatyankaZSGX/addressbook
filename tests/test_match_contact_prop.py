__author__ = 'ZSGX'

import re

def test_match_tel_with_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_props_from_editpage(0)
    assert contact_from_homepage.tel == merge_tel_like_homepage(contact_from_editpage)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_tel_like_homepage(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.homephone, contact.mobilephone,
                                                                 contact.workphone, contact.phone2]))))

