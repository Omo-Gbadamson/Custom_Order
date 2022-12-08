from flask import Flask
from src.database.db import start_db
from src.urls.routes import start_route
from flask_restful import Api


app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = MONGO_URI ={
    "db": "custom-order-db",
    "host": "localhost",
    "port": 27017
}


api = Api(app,)

start_db(app)
start_route(api)


app.run(host="127.0.0.1", port=5000, debug=True)
