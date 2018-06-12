from DataAccess import DB
from flask import render_template,session,Blueprint,Response,make_response,request,redirect,url_for,abort,flash

view = Blueprint("Index", __name__)  # , template_folder="templates"


@view.route('/')
def hello_world():
    return render_template("hello.html")


@view.route('/GetUsers/<userId>')
def GetUsersByUserId(userId):
    #redirect
    if userId =="1":
        flash("this is message")
        return redirect(url_for("Index.hello_world"))
    #abort
    elif userId=="2":
        abort(500)
    #render_template
    else:
        users = DB.Users.find({"UserId": userId})
        return render_template("index.html", users=users)


@view.route('/GetUsers')
def GetUsers():
    users = DB.Users.find({})
    return render_template("index.html", users=users)


@view.route('/setcookie/<userid>')
def setcookie(userid):
    users = DB.Users.find({})
    res = make_response(render_template("index.html", users=users))
    res.set_cookie('userID', userid)
    return res



@view.route('/getcookie')
def getcookie():
    userid = request.cookies.get('userID')
    return render_template("hello.html",userid=userid)



@view.route('/setsession/<userid>')
def setsession(userid):
    session["userId"] = userid
    return render_template("hello.html",userid=userid)



@view.route('/getsession')
def getsession():
    userid = session["userId"]
    return render_template("hello.html",userid=userid)

