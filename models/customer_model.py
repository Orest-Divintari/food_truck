from db import db

class CustomerModel(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    food_preference = db.Column(db.String(80))

    def __init__(self, longitude, latitude, food_preference):
        self.longitude = longitude
        self.latitude = latitude
        self.food_preference = food_preference

    @staticmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id)

    @staticmethod
    def find_by_coordinates(cls, longitude, latitude):
        pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
