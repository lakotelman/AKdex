from csv import reader
from app.database import db


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sci_name = db.Column(db.String(100))
    given_name = db.Column(db.String(100))
    family = db.Column(db.String(100))
    order = db.Column(db.String(100))


def build_animal_db(path: str) -> None:
    result = Animal.query.where().all()

    if len(result) > 0:
        return

    with open(path) as csvfile:
        animalreader = list(reader(csvfile))
        for animal in animalreader:
            a = Animal(
                sci_name=animal[0],
                given_name=animal[2],
                family=animal[3],
                order=animal[4],
            )
            db.session.add(a)
        db.session.commit()
