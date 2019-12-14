from db import db


class FoodTruckModel(db.Model):
    __tablename__ = 'food_trucks'
    id = db.Column(db.Integer, primary_key=True)
    current_longitude = db.Column(db.Float)
    current_latitude = db.Column(db.Float)
    destination_longitude = db.Column(db.Float)
    destination_latitude = db.Column(db.Float)
    food_list = db.relationship('FoodListModel')

    def __init__(self, food_truck_id, current_longitude, current_latitude,
                 destination_longitude = None, destination_latitude = None ):
        self.id = food_truck_id
        self.current_longitude = current_longitude
        self.current_latitude = current_latitude
        self.destination_latitude = destination_latitude
        self.destination_longitude = destination_longitude

    @staticmethod
    def find_by_id(cls, food_truck_id):
        return cls.query.filter_by(id=food_truck_id).first()

    @staticmethod
    def find_by_coordinates(cls, longitude, latitude):
        pass

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

