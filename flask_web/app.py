from flask import Flask
from Views import Index

app = Flask(__name__,static_folder="/templates")
app.register_blueprint(Index.view)
app.secret_key ='my super secret key'.encode('utf8')

if __name__ == '__main__':
    app.run( host='127.0.0.1', port=8000, debug=True )
