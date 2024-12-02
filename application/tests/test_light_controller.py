from unittest.mock import Mock
from unittest.mock import patch

from application.light_controller import setup_mqtt_callbacks
from application.light_controller import handle_circadian_rhythm_message


def test_handle_connect():
    mqtt_client = Mock()
    setup_mqtt_callbacks(mqtt_client)
    mqtt_client.on_connect.assert_called()


def test_handle_circadian_rhythm_message():
    with patch('builtins.print') as mock_print:
        handle_circadian_rhythm_message('sunrise')
        mock_print.assert_called_with('Received circadian rhythm message: sunrise')
