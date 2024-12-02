from unittest.mock import (
    Mock,
    patch,
)

from application.light_controller import setup_mqtt_callbacks
from application.light_controller import (
    handle_circadian_rhythm_message,
    handle_motion_sensor_message,
)


def test_handle_connect():
    mqtt_client = Mock()
    setup_mqtt_callbacks(mqtt_client)
    mqtt_client.on_connect.assert_called()
    mqtt_client.on_message.assert_called()


def test_handle_circadian_rhythm_message():
    with patch('builtins.print') as mock_print:
        handle_circadian_rhythm_message('sunrise')
        mock_print.assert_any_call("Adjusting light to intensity: 50%")


def test_handle_motion_sensor_message():
    with patch('builtins.print') as mock_print:
        handle_motion_sensor_message('motion_detected')
        mock_print.assert_called_with('Received motion sensor message: motion_detected')
