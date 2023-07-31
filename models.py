from app import db

class Location(db.Model):
    __tablename__= "location"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    founded = db.Column(db.Integer)

    def __repr__(self):
        return f'<location {self.id}: {self.name}: {self.founded}'

class Animal(db.Model):
    __tablename__ = "animal"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    species = db.Column(db.String(64))
    owner = db.Column(db.String(64))

    def __repr__ (self):
        return f'<Animal {self.id}: {self.name}: {self.species}: {self.owner}'

class Vet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))

    def __repr__ (self):
        return f'<Vet {self.id}: {self.name}'
    
class Home(db.Model):
    return None
