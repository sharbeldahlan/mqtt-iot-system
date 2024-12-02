from flask import Flask
from flask_mqtt import Mqtt

from application.config import Config


# Initialize the Flask app and load settings from Config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-MQTT client
mqtt_client = Mqtt(app)
