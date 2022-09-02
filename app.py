from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from models import Contact
from forms import ContactForm

@app.route("/contact.html", methods=["POST", "GET"])
def contact():
    form = ContactForm()
    return render_template("contact.html", title ="Contact Us", form=form)

@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html", title="Ngunnawal Country")


if __name__ == '__main__':
    app.run()
