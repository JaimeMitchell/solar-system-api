from app import db


class Planet(db.Model):  # The class Planet inherits from db.Model from SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
