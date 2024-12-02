from typing import Any


def handle_circadian_rhythm_message(payload: str) -> None:
    """Handle circadian rhythm messages and adjust light intensity."""
    print(f'Received circadian rhythm message: {payload}')


def setup_mqtt_callbacks(mqtt_client: Any) -> None:
    """Set up MQTT subscriptions and callbacks."""
    @mqtt_client.on_connect()
    def handle_connect(client: Any, userdata: Any, flags: Any, rc: int) -> None:
        """Handle connection and subscribe to topics."""
        print('Connected to MQTT broker successfully')
        mqtt_client.subscribe('iot/lights/circadian_rhythm')

    @mqtt_client.on_message()
    def handle_mqtt_message(client: Any, userdata: Any, message: Any) -> None:
        """Handle incoming messages."""
        payload: str = message.payload.decode()
        handle_circadian_rhythm_message(payload)
