from app import db


class Planet(db.Model):  # The class Planet inherits from db.Model from SQLAlchemy
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            description=self.description,
            temperature=self.temperature
        )
    # can also return traditional dictionary:
    # return {
        # id=self.id,
        # name=self.name,
        # description=self.description,
        # temperature=self.temperature
        # }
