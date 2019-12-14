from db import db


class FoodListModel(db.Model):
    __tablename__ = 'food_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    food_truck_id = db.Column(db.Integer, db.ForeignKey('food_truck_id'))
    db.relationship('FoodTruckModel')

    def __init__(self, food_name, food_truck_id):
        self.name = food_name
        self.food_truck_id = food_truck_id

    @staticmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



