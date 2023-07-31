from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://brandonnoone@localhost:5432/Hyrule_Health_Care"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/home")
def home():
    return render_template("index.jinja", title="Hyrule Health Care")

@app.route("/home/locations")
def location():
    return render_template("index.jinja", title="Hyrule locations")

app.route("/home/locations/<id>")
def location_id():
    return render_template("index.jinja", title="These are the Locations to choose from", location=location)

@app.route("/home/vets")
def vet():
    return render_template("index.jinja", title= "Hyrule vets")

