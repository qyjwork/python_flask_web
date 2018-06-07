from flask import Flask, render_template
from Views import Index


app = Flask(__name__,static_folder="/templates")
app.register_blueprint(Index.view)



if __name__ == '__main__':
    app.run(debug=True)
