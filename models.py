from app import db

class location(db.Model):
    __tablename__= "location"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    founded = db.Column(db.Integer)

    def __repr__(self):
        return f'<location {self.id}: {self.name}: {self.founded}'

class animal(db.Model):
    __tablename__ = "animal"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    species = db.Column(db.String(64))
    owner = db.Column(db.String(64))

class vet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    
