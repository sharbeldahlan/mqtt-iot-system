from unittest.mock import patch

from application.constants import Topic
from application.publishers.circadian_rhythm_publisher import publish_circadian_phase


@patch('application.publishers.circadian_rhythm_publisher.client')
def test_publish_circadian_phase(mock_client):
    publish_circadian_phase('sunrise')
    mock_client.publish.assert_called_once_with(
        Topic.CIRCADIAN_RHYTHM, 'sunrise'
    )
