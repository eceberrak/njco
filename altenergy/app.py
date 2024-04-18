from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os, io
from werkzeug.utils import secure_filename
import csv
from sqlalchemy import desc, asc
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/biofuel")
def biofuel():
    return render_template("biofuel.html")

@app.route("/fuelcell")
def fuelcell():
    return render_template("fuelcell.html")

@app.route("/solar")
def solar():
    return render_template("solar.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/workscited")
def cite():
    return render_template("cite.html")

if __name__ == "__main__":
    app.secret_key = "super_secret_key"  # Change this to a random, secure key
    app.run(debug=True)
