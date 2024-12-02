from typing import Any
from typing import Callable

from application.constants import Topic

# Mapping circadian phases to light intensities
PHASE_TO_INTENSITY: dict[str, int] = {
    'sunrise': 50,
    'morning': 100,
    'sunset': 30,
    'night': 5,
}


def handle_circadian_rhythm_message(payload: str) -> None:
    """Handle circadian rhythm messages and adjust light intensity."""
    print(f'\nReceived circadian rhythm message: {payload}')
    light_intensity: int = PHASE_TO_INTENSITY.get(payload, 0)
    print(f'Adjusting light to intensity: {light_intensity}%')


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
