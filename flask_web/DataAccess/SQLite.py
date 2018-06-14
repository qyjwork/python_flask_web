# coding=utf-8
import sqlite3

class sqlite:

    def __init__(self,databasename="database",check_same_thread=False):
        self.db = sqlite3.connect(databasename+'.db', check_same_thread=check_same_thread)

    def createtable(self,sql):
        self.db.execute(sql)#('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')



