from flask import Flask
from flask_restful import Api
from db import db
from flask import render_template
from flask_jwt import JWT
# from security import authenticate, identity
import pyowm
from uszipcode import SearchEngine
# search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database
# zipcode = search.by_coordinates(39.122229, -77.133578, radius = 30, returns = 5)
#
# for zc in zipcode:
#     print(zc)
#
# app = Flask(__name__)
# owm = pyowm.OWM('cc5795a90251a8f01d937c8392578570') # weather api key
#
# observation = owm.weather_at_place('London,GB')
# w = observation.get_weather()
# temp = w.get_temperature('celsius')
# print(temp)
#
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'food_truck'
api = Api(app)
# jwt = JWT(app, authenticate, identity)



#
# import stomp
# import time
#
#
# class MyListener(stomp.ConnectionListener):
#
#     def on_error(self, headers, message):
#         print(f'received an error {message}')
#
#     def on_message(self, headers, message):
#         print(f'received a message {message}')
#
#
# conn = stomp.Connection()
# conn.set_listener('', MyListener())
# conn.start()
# conn.connect('admin', 'password', wait=True)
# conn.subscribe(destination='/queue/qq', id=1, ack='auto')
#

# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route('/')
def home():
    return render_template('/index.html')


@app.route('/sign_up')
def sign_up():
    return render_template('/sign_up.html')


@app.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@app.route('/sign_up/customer')
def sign_up_customer():
    return render_template('/customer_sign_up.html')


@app.route('customer/register')
def customer_register():
    return render_template('/customer_sign_up.html')


@app.route('/sign_up/food_truck_owner')
def sign_up_fto():
    return render_template('/fto_sign_up.html')
# maybe i will have to remove the condition if __name__ == 'main', but keep the commands inside
if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
