import paho.mqtt.client as mqtt

from application.config import Config


# Set up MQTT client
client = mqtt.Client()
client.username_pw_set(Config.MQTT_USERNAME, Config.MQTT_PASSWORD)
client.connect(Config.MQTT_BROKER_URL, Config.MQTT_BROKER_PORT, Config.MQTT_KEEPALIVE)


# Simulate publishing circadian rhythm data
def publish_circadian_phase(phase: str) -> None:
    """
    Publish circadian phase to the MQTT broker.
    """
    client.publish('iot/lights/circadian_rhythm', phase)
    print(f'Published on topic --> "iot/lights/circadian_rhythm": {phase}')
