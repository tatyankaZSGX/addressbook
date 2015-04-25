__author__ = 'ZSGX'

import jsonpickle
import getopt
import sys
import os.path
import string
from model.contact import Contact
import random

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["groups_count","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data\contact.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(middlename="middlename1234")]+\
           [Contact(firstname=random_string("", 10), middlename=random_string("", 10), lastname=random_string("",10),
                    nickname=random_string("", 10), title=random_string("", 10), company=random_string("", 10),
                    address=random_string("", 10), homephone=random_string("", 10), mobilephone=random_string("",10),
                    workphone=random_string("", 10), fax=random_string("", 10), email2=random_string("", 10),
                    email3=random_string("", 10), homepage=random_string("", 10), address2=random_string("", 10),
                    phone2=random_string("", 10), notes=random_string("", 100), bday=9, bmonth=6, byear=1961,
                    aday=26, amonth=10, ayear=1985, path="C:\\img.jpg")
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))