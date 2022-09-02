from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", title="Ngunnawal Country")


if __name__ == '__main__':
    app.run()
