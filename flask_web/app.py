from flask import Flask
from Controller import MongoDBController, SQliteController
from DataAccess.SQLite import sqlite

app = Flask(__name__,static_folder="/templates")
app.register_blueprint(MongoDBController.view)
app.register_blueprint(SQliteController.view)
app.secret_key ='my super secret key'.encode('utf8')




if __name__ == '__main__':
    # sql = sqlite()
    # sql.__init__()
    # sql.createtable('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
    app.run( host='127.0.0.1', port=8000, debug=True )

