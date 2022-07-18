from flask import render_template, request
from app.models.animal import Animal,build_animal_db
from . import bp as app 
from pathlib import Path


CWD = Path(__file__).parent

CSV = CWD.parent.parent/"models"/"mammals.csv"

@app.before_app_first_request
def before_first_request():
    build_animal_db(CSV)


@app.route("/")
def home(): 
    animal = Animal.query.all()
    context = { 
        "animals": animal
    }
    return render_template("index.html", **context)

@app.route("my-dex")
def my_dex(): 
    return render_template("my_dex.html")

@app.route("/add", methods=["GET", "POST"])
def add_to_dex():
    return "Hmm"