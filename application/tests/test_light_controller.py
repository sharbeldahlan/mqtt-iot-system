from unittest.mock import Mock

from application.light_controller import setup_mqtt_callbacks


def test_handle_connect():
    mqtt_client = Mock()

    setup_mqtt_callbacks(mqtt_client)

    mqtt_client.on_connect.assert_called()
