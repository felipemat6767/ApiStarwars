from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(10), nullable = False)
    email = db.Column(db.String(20), nullable = False)
    isActive = db.Column(db.Boolean, default = False)

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "password": self.password,
            "email": self.email,
            "isActive": self.isActive
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Character (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    height = db.Column(db.String(10), nullable = False)
    mass = db.Column(db.String(20), nullable = False)
    hair_color = db.Column(db.String(100), nullable = False)
    skin_color = db.Column(db.String(100), nullable = False)
    eye_color = db.Column(db.String(100), nullable = False)
    birthyear = db.Column(db.String(100), nullable = False)
    gender = db.Column(db.String(20), nullable = False)
    homeworld = db.Column(db.String(50), nullable = False)
    films = db.Column(db.String(100), nullable = False)
    species = db.Column(db.String(20), nullable = False)
    vehicles = db.Column(db.String(100), nullable = False)
    starships = db.Column(db.String(100), nullable = False)
    created = db.Column(db.String(50), nullable = False)
    edited = db.Column(db.String(50), nullable = False)
    url = db.Column(db.String(50), nullable = False)
   

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birthyear": self.birthyear,
            "gender": self.gender,
            "homeworld": self.homeworld,
            "films": self.films,
            "species": self.species,
            "vehicles": self.vehicles,
            "starships": self.starships,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Planets (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    rotation_period = db.Column(db.String(10), nullable = False)
    orbital_period = db.Column(db.String(20), nullable = False)
    diameter = db.Column(db.String(100), nullable = False)
    climate = db.Column(db.String(100), nullable = False)
    gravity = db.Column(db.String(100), nullable = False)
    terrain = db.Column(db.String(100), nullable = False)
    surface_water = db.Column(db.String(20), nullable = False)
    population = db.Column(db.String(20), nullable = False)
    residents = db.Column(db.String(20), nullable = False)
    films = db.Column(db.String(50), nullable = False)
    created = db.Column(db.String(50), nullable = False)
    edited = db.Column(db.String(50), nullable = False)
    url = db.Column(db.String(50), nullable = False)
   

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "residents": self.residents,
            "films": self.films,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }

class Starships (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    model = db.Column(db.String(10), nullable = False)
    manufacturer = db.Column(db.String(20), nullable = False)
    cost_in_credits = db.Column(db.String(100), nullable = False)
    length = db.Column(db.String(100), nullable = False)
    max_atmosphering_speed = db.Column(db.String(100), nullable = False)
    crew = db.Column(db.String(100), nullable = False)
    passengers = db.Column(db.String(20), nullable = False)
    cargo_capacity = db.Column(db.String(20), nullable = False)
    consumables = db.Column(db.String(20), nullable = False)
    hyperdrive_rating = db.Column(db.String(50), nullable = False)
    MGLT = db.Column(db.String(50), nullable = False)
    starship_class = db.Column(db.String(50), nullable = False)
    pilots = db.Column(db.String(50), nullable = False)
    created = db.Column(db.String(50), nullable = False)
    edited = db.Column(db.String(50), nullable = False)
    url = db.Column(db.String(50), nullable = False)
   

    def __repr__(self):
        return "<User r%/>" % self.id

    def serialize(self): 
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "length": self.length,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "hyperdrive_rating": self.hyperdrive_rating,
            "MGLT": self.MGLT,
            "starship_class": self.starship_class,
            "pilots": self.pilots,
            "created": self.created,
            "edited": self.edited,
            "url": self.url
        }

    def serialize_username(self): 
        return {
            "id": self.id,
            "name": self.name
        }