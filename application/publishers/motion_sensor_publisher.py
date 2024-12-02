from typing import Any

import paho.mqtt.client as mqtt

from application.config import Config
from application.constants import Topic


# Set up MQTT client
client = mqtt.Client()
client.username_pw_set(Config.MQTT_USERNAME, Config.MQTT_PASSWORD)
client.connect(Config.MQTT_BROKER_URL, Config.MQTT_BROKER_PORT, Config.MQTT_KEEPALIVE)


# Simulate publishing motion sensor data
def publish_motion_data() -> None:
    motion_data: dict[str, Any] = {"motion_detected": True}
    # retain is False for event-driven topics like motion detection
    client.publish(Topic.MOTION, str(motion_data), qos=0, retain=False)
    print(f'Published on topic --> {Topic.MOTION}: {motion_data}')
