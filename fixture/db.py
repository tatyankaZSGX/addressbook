__author__ = 'ZSGX'

import mysql.connector

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user= user
        self.password = password
        self.connection = mysql.connector.connect(host=host, name=name, user=user, password=password)

    def destrioy(self):
        self.connection.close()