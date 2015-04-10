__author__ = 'ZSGX'

from model.contact import Contact
import random
import string

constant = [Contact(firstname="Michael", middlename="J.", lastname="Fox", nickname="Marti",
                    title="Actor", company="Hollywood", address="Los Angeles", homephone="911",
                    mobilephone="9911", workphone="999111", fax="919191", email2="mail2@mail.ff",
                    email3="mail3@mail.ff", homepage="fox.ff", address2="adr2", phone2="02",
                    notes="Back to the Future", bday=9, bmonth=6, byear=1961, aday=26, amonth=10,
                    ayear=1985, path="C:\\img.jpg")]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

randdata = [Contact(firstname=random_string("", 10), middlename=random_string("", 10), lastname=random_string("", 10),
            nickname=random_string("", 10), title=random_string("", 10), company=random_string("", 10),
            address=random_string("", 10), homephone=random_string("", 10), mobilephone=random_string("", 10),
            workphone=random_string("", 10), fax=random_string("", 10), email2=random_string("", 10),
            email3=random_string("", 10), homepage=random_string("", 10), address2=random_string("", 10),
            phone2=random_string("", 10), notes=random_string("", 100), bday=9, bmonth=6, byear=1961, aday=26,
            amonth=10, ayear=1985, path="C:\\img.jpg")
    for i in range(2)]
