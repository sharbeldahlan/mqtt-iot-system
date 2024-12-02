import threading

from flask import Flask
from flask_mqtt import Mqtt

from application.config import Config
from application.light_controller import setup_mqtt_callbacks
from application.publishers.circadian_rhythm_publisher import run_circadian_rhythm_publisher
from application.publishers.motion_sensor_publisher import run_motion_sensor_publisher

# Initialize the Flask app and load settings from Config
app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-MQTT client
mqtt_client = Mqtt(app)

# Run publishers (mock iot devices)
circadian_rhythm_publisher_thread = threading.Thread(target=run_circadian_rhythm_publisher, daemon=True)
circadian_rhythm_publisher_thread.start()
motion_sensor_publisher_thread = threading.Thread(target=run_motion_sensor_publisher, daemon=True)
motion_sensor_publisher_thread.start()

# Set up MQTT subscriptions and callbacks
setup_mqtt_callbacks(mqtt_client)
