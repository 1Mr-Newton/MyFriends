import email
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SECRET_KEY"] = "my secret key that is very difficult for hackers to hack"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:password123@localhost/our_users"

db = SQLAlchemy(app)
# create form class
class NamerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


# create db model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # create a return string
    def __repr__(self):
        return "<Name %r>" % self.name


@app.route("/user/add", methods=["GET", "POST"])
def add_user():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        # print(user)
        # print(form.email.data)
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash("User Added Successfully")
        else:
            flash("Email Already Exists!")

        name = form.name.data
        form.name.data = ""
        form.email.data = ""
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html", form=form, name=name, our_users=our_users)


@app.route("/name", methods=["GET", "POST"])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form Submitted Successfully")

    return render_template("name.html", name=name, form=form)


@app.route("/", methods=["POST", "GET"])
def index():
    flash("Welcome to my website")
    return render_template("index.html")


@app.route("/user/<name>")
def user(name):
    user_name = name

    return render_template("user.html", user_name=user_name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
