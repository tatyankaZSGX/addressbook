__author__ = 'ZSGX'


class Contacttext:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, address, homephone, mobilephone, workphone, fax, email2, email3, homepage, address2, phone2, notes):
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

class Contactdate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

