from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from register import Register
from refill import Refill
from classify_feeling import ClassifyFeeling
app = Flask(__name__)
api = Api(app)

api.add_resource(Register,"/register")
api.add_resource(Refill,"/refill")
api.add_resource(ClassifyFeeling,"/classify_feeling")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
