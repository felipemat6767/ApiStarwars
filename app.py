import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, User, Character, Planets, Starships
from flask_migrate import Migrate

Basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(Basedir, "test.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["ENV"] = "developement"
app.config["Debug"] = True

Migrate(app, db)
db.init_app(app)

@app.route("/")
def Home():
  return jsonify("Hola Mundo")

@app.route("/user", methods = ["POST"])
def user():
  user = User()
  user.name = request.json.get("name")
  user.password = request.json.get("password")
  user.email = request.json.get("email")
  user.isActive = request.json.get("isActive")
  db.session.add(user)
  db.session.commit()
  return jsonify(user.serialize()), 200

  


@app.route("/characters", methods = ["POST"])
def character():
  character = Character()
  character.name = request.json.get("name")
  character.height = request.json.get("height")
  character.mass = request.json.get("mass")
  character.hair_color = request.json.get("hair_color")
  character.skin_color = request.json.get("skin_color")
  character.eye_color = request.json.get("eye_color")
  character.birthyear = request.json.get("birthyear")
  character.gender = request.json.get("gender")
  character.homeworld = request.json.get("homeworld")
  character.films = request.json.get("films")
  character.species = request.json.get("species")
  character.vehicles = request.json.get("vehicles")
  character.starships = request.json.get("starships")
  character.created = request.json.get("created")
  character.edited = request.json.get("edited")
  character.url= request.json.get("url")

  db.session.add(character)
  db.session.commit()
  return jsonify(character.serialize()), 200


@app.route("/planets", methods = ["POST"])
def planets():
  planets = Planets()
  planets.name = request.json.get("height")
  planets.masst = request.json.get("mass")
  planets.hair_color = request.json.get("hair_color")
  planets.skin_color = request.json.get("skin_color")
  planets.eye_color = request.json.get("eye_color")
  planets.birthyear = request.json.get("birthyear")
  planets.gender = request.json.get("gender")
  planets.homeworld = request.json.get("homeworld")
  planets.films = request.json.get("films")
  planets.species = request.json.get("species")
  planets.vehicles = request.json.get("vehicles")
  planets.starships = request.json.get("starships")
  planets.created = request.json.get("created")
  planets.edited = request.json.get("edited")
  planets.url= request.json.get("url")

  db.session.add(planets)
  db.session.commit()
  return jsonify(planets.serialize()), 200

@app.route("/starships", methods = ["POST"])
def starships():
  starships = Starships()
  starships.name = request.json.get("height")
  starships.model = request.json.get("model")
  starships.manufacturer = request.json.get("manufacturer")
  starships.cost_in_credits = request.json.get("cost_in_credits")
  starships.length = request.json.get("length")
  starships.max_atmosphering_speed = request.json.get("max_atmosphering_speed")
  starships.crew = request.json.get("crew")
  starships.passengers = request.json.get("passengers")
  starships.cargo_capacity = request.json.get("cargo_capacity")
  starships.consumables = request.json.get("consumables")
  starships.hyperdrive_rating = request.json.get("hyperdrive_rating")
  starships.MGLT = request.json.get("MGLT")
  starships.starship_class = request.json.get("starship_class")
  starships.pilots= request.json.get("pilots")
  starships.url= request.json.get("url")

  db.session.add(starships)
  db.session.commit()
  return jsonify(starships.serialize()), 200

if __name__ == "__main__":
    app.run(host ="localhost", port = 8080)


if __name__ == "__main__":
    app.run(host ="localhost", port = 8080)


  