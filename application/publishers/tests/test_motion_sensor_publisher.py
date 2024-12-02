from unittest.mock import patch

from application.constants import Topic
from application.publishers.motion_sensor_publisher import publish_motion_data


@patch('application.publishers.motion_sensor_publisher.client')
def test_publish_motion_data(mock_client):
    publish_motion_data()
    mock_client.publish.assert_called_once_with(
        Topic.MOTION, "{'motion_detected': True}", qos=0, retain=False
    )
