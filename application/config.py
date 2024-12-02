import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Settings for the MQTT Client
    MQTT_BROKER_URL = os.getenv("MQTT_BROKER_URL")
    MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", 1883))
    MQTT_KEEPALIVE = int(os.getenv("MQTT_KEEPALIVE", 5))
    MQTT_CLIENT_ID = os.getenv("MQTT_CLIENT_ID", "default_client_id")
    MQTT_USERNAME = os.getenv("MQTT_USERNAME", '')
    MQTT_PASSWORD = os.getenv("MQTT_PASSWORD", '')
    MQTT_TLS_ENABLED = os.getenv("MQTT_TLS_ENABLED", "False").lower() == "true"
