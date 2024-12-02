from flask import Flask
from flask_mqtt import Mqtt

from application.config import Config
from application.light_controller import setup_mqtt_callbacks
from application.publishers.circadian_rhythm_publisher import publish_circadian_phase


# Initialize the Flask app and load settings from Config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-MQTT client
mqtt_client = Mqtt(app)

# Run publisher (mock iot devices)
publish_circadian_phase('sunrise')

# Set up MQTT subscriptions and callbacks
setup_mqtt_callbacks(mqtt_client)
