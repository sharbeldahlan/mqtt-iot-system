import pytest
from unittest.mock import patch

from application.constants import Topic
from application.publishers.circadian_rhythm_publisher import (
    publish_circadian_phase,
    run_circadian_rhythm_publisher,
    CIRCADIAN_PHASES,
)


@pytest.fixture
def mock_mqtt_client():
    with patch('application.publishers.circadian_rhythm_publisher.client') as mock_client:
        yield mock_client


@pytest.fixture
def mock_scheduler():
    with patch('application.publishers.circadian_rhythm_publisher.scheduler') as mock_scheduler:
        yield mock_scheduler


@pytest.mark.parametrize('current_phase, delay, expected_next_phase', [
    ('sunrise', 6, 'morning'),
    ('morning', 6, 'sunset'),
    ('sunset', 6, 'night'),
    ('night', 6, 'sunrise'),
])
def test_publish_circadian_phase(mock_mqtt_client, mock_scheduler, current_phase, delay, expected_next_phase):
    """
    Test that the correct phase is published and the next phase is scheduled.
    """
    publish_circadian_phase(current_phase, delay)

    # Verify publish call
    mock_mqtt_client.publish.assert_called_once_with(Topic.CIRCADIAN_RHYTHM, current_phase)

    # Verify scheduling of the next phase
    expected_next_delay = delay
    mock_scheduler.enter.assert_called_once_with(
        expected_next_delay, 1, publish_circadian_phase, argument=(expected_next_phase, expected_next_delay)
    )


def test_run_circadian_rhythm_publisher(mock_scheduler):
    """
    Test that the circadian rhythm publisher schedules the initial phase and starts the scheduler.
    """
    run_circadian_rhythm_publisher()

    # Verify that the initial phase is scheduled
    initial_phase, initial_delay = CIRCADIAN_PHASES[0]
    mock_scheduler.enter.assert_called_once_with(
        0, 1, publish_circadian_phase, argument=(initial_phase, initial_delay)
    )

    # Verify that the scheduler is started
    mock_scheduler.run.assert_called_once()
