from app import db

class Planet(db.Model): #The class Planet inherits from db.Model from SQLAlchemy
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String)
    description = db.Column(db.String)
    temperature = db.Column(db.Integer)
    