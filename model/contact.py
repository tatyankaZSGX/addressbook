__author__ = 'ZSGX'


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, fax=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None, bday=None, bmonth=None, byear=None, aday=None,
                 amonth=None, ayear=None, path=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.filepath = path
        self.id = id

    def __repr__(self):
        return"%s, %s" % (self.id, self.lastname)