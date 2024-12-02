import pytest
from unittest.mock import Mock

from application.light_controller import (
    handle_circadian_rhythm_message,
    handle_motion_sensor_message,
    setup_mqtt_callbacks,
)


def test_handle_connect():
    mqtt_client = Mock()
    setup_mqtt_callbacks(mqtt_client)
    mqtt_client.on_connect.assert_called()
    mqtt_client.on_message.assert_called()


@pytest.mark.parametrize('payload, expected_intensity', [
    ('sunrise', 50),
    ('morning', 100),
    ('sunset', 30),
    ('night', 5),
    ('unknown', 0),
])
def test_handle_circadian_rhythm_message(payload, expected_intensity, capsys):
    handle_circadian_rhythm_message(payload)
    captured = capsys.readouterr()
    assert f'Received circadian rhythm message: {payload}' in captured.out
    assert f'Adjusting light to intensity: {expected_intensity}%' in captured.out


def test_handle_motion_sensor_message(capsys):
    handle_motion_sensor_message('motion_detected')
    captured = capsys.readouterr()
    assert 'Received motion sensor message: motion_detected' in captured.out
    assert 'Adjusting light to intensity: 100%' in captured.out
