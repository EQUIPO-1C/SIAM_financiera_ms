from flask import Flask
from flask_pymongo import pymongo
from app import app
import os
from dotenv import load_dotenv


load_dotenv()

user = os.environ.get("DB_USER")
pswd = os.environ.get("DB_PSWD")


CONNECTION_STRING = "mongodb+srv://{}:{}@procesoinscluster.kb4ixgp.mongodb.net/?retryWrites=true&w=majority".format(user, pswd)
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('financiera_db')
