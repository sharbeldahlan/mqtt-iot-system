from typing import Any
from typing import Callable

from application.constants import Topic


def handle_circadian_rhythm_message(payload: str) -> None:
    """Handle circadian rhythm messages and adjust light intensity."""
    print(f'Received circadian rhythm message: {payload}')


def handle_motion_sensor_message(payload: str) -> None:
    """Handle motion sensor messages and adjust light intensity."""
    print(f'Received motion sensor message: {payload}')


def setup_mqtt_callbacks(mqtt_client: Any) -> None:
    """Set up MQTT subscriptions and callbacks."""
    @mqtt_client.on_connect()
    def handle_connect(client: Any, userdata: Any, flags: Any, rc: int) -> None:
        """Handle connection and subscribe to topics."""
        print('Connected to MQTT broker successfully')
        mqtt_client.subscribe(Topic.CIRCADIAN_RHYTHM)
        mqtt_client.subscribe(Topic.MOTION)
        print(f'Subscribed to topics {Topic.CIRCADIAN_RHYTHM} and {Topic.MOTION}')

    @mqtt_client.on_message()
    def handle_mqtt_message(client: Any, userdata: Any, message: Any) -> None:
        """Handle incoming messages."""
        TOPIC_HANDLERS: dict[str, Callable[[str], None]] = {
            Topic.CIRCADIAN_RHYTHM: handle_circadian_rhythm_message,
            Topic.MOTION: handle_motion_sensor_message,
        }

        topic: str = message.topic
        payload: str = message.payload.decode()

        handler: Callable[[str], None] | None = TOPIC_HANDLERS.get(topic)
        if handler:
            handler(payload)
        else:
            print(f'Unknown topic: {topic}')
