import app
from DataAccess import DB
from flask import render_template, Blueprint

view = Blueprint("Index", __name__) #, template_folder="templates"


@view.route('/')
def hello_world():
    return render_template("hello.html")


@view.route('/GetUsers/<userId>')
def GetUsersByUserId(userId):
    users = DB.Users.find({"U refusing to merge unrelated historiesserId": userId})
    if users.count() ==0:
        DB.Users.insert({"UserId":"5F38FF88D6DA4965B902016261F55A83","Age":20})
        DB.Users.insert({"UserId":"2401A71D879E49F0BE68B63FA410EE7A","Age":30})
    return render_template("index.html", users=users)


@view.route('/GetUsers')
def GetUsers():
    users = DB.Users.find({})
    return render_template("index.html", users=users)