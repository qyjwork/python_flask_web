# coding=utf-8
from flask import render_template, Blueprint
from DataAccess import SQLite
import sqlite3

view = Blueprint("Sqlite", __name__)  # , template_folder="templates"
sql = SQLite.sqlite()

@view.route('/sqlite')
def hello_world():
    return render_template("hello.html", userid="sqlite")



@view.route('/adduser')
def adduser():

    with sql.db as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,addr,city,pin)  VALUES(?, ?, ?, ?)",("N1","ADDR1","SH","20000") )
            con.commit()
            return render_template("hello.html", userid="sqlite")
        finally:
            pass


@view.route('/getusers')
def getusers():
    with sql.db as con:
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("select * from students ")
        users = cur.fetchall();
    return render_template("users.html", users = users)