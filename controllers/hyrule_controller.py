from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Location, Animal, Vet, Home
# Import models

hyrule_blueprint = Blueprint("hyrule", __name__)

# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)

# @hyrule_blueprint.route("/home/location/<id>")
# def location_show(id):
#     location_obj = loaction.query.get(id)
#     return render_template("/home/location/show.jinja", location=location_obj)

#fix location


@hyrule_blueprint.route("/home")
def home():
    homepage = Home.query.all()
    return render_template("index.jinja", title="Hyrule Health Care", homepage=home)

@hyrule_blueprint.route("/home/locations")
def location():
    return render_template("index.jinja", title="Hyrule locations")

@hyrule_blueprint.route("/home/locations/<id>")
def location_id():
    return render_template("index.jinja", title="These are the Locations to choose from", location=location)

@hyrule_blueprint.route("/home/vets")
def vet():
    return render_template("index.jinja", title= "Hyrule vets")

