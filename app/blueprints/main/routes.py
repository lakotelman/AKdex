from flask import redirect, render_template, request, url_for
from flask_login import current_user
from app.blueprints.auth import routes
from app.models.animal import Animal,build_animal_db
from app.models.user import User
from . import bp as app
from app.database import db
from pathlib import Path


CWD = Path(__file__).parent

CSV = CWD.parent.parent/"models"/"mammals.csv"

@app.before_app_first_request
def before_first_request():
    build_animal_db(CSV)


@app.route("/")
def home():
    if not current_user.is_authenticated: 
        return redirect(url_for("auth.login"))
    animal = Animal.query.all()
    context = { 
        "animals": animal
    }
    return render_template("index.html", **context)

@app.route("/my-dex")
def my_dex(): 
    if not current_user.is_authenticated: 
        return redirect(url_for("auth.login"))
    return render_template("my_dex.html")

@app.route("/add", methods=["POST"])
def add():
    collection = current_user.animals
    animal_id = request.form.get('animal')
    animal = Animal.query.filter_by(id=animal_id).first()
    collection.append(animal)
    db.session.commit()
    return render_template("my_dex.html")