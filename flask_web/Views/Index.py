import app
from DataAccess import DB
from flask import render_template, Blueprint

view = Blueprint("Index", __name__) #, template_folder="templates"


@view.route('/')
def hello_world():
    return render_template("hello.html")


@view.route('/GetUsers/<userId>')
def GetUsersByUserId(userId):
    users = DB.Users.find({"UserId": userId})
    return render_template("index.html", users=users)


@view.route('/GetUsers')
def GetUsers():
    users = DB.Users.find({})
    return render_template("index.html", users=users)