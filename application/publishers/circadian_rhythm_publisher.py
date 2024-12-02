import sched
import time

import paho.mqtt.client as mqtt

from application.config import Config
from application.constants import Topic


# Set up MQTT client
client = mqtt.Client()
client.username_pw_set(Config.MQTT_USERNAME, Config.MQTT_PASSWORD)
client.connect(Config.MQTT_BROKER_URL, Config.MQTT_BROKER_PORT, Config.MQTT_KEEPALIVE)

# Initialize scheduler
scheduler = sched.scheduler(time.time, time.sleep)

# Simulated time phases of the day (but 24 seconds instead of 24 hours)
CIRCADIAN_PHASES: list[tuple[str, int]] = [
    ('sunrise', 6),  # 6 seconds (morning)
    ('morning', 6),  # 6 seconds (daylight)
    ('sunset', 6),  # 6 seconds (evening)
    ('night', 6),  # 6 seconds (nighttime)
]


# Simulate publishing circadian rhythm data
def publish_circadian_phase(phase: str, delay: int) -> None:
    """
    Publish circadian phase to the MQTT broker and schedule the next phase.
    """
    client.publish(Topic.CIRCADIAN_RHYTHM, phase)
    print(f'\nPublished on topic --> {Topic.CIRCADIAN_RHYTHM}: {phase}')

    # Schedule the next phase
    next_phase_index = (CIRCADIAN_PHASES.index((phase, delay)) + 1) % len(CIRCADIAN_PHASES)
    next_phase, next_delay = CIRCADIAN_PHASES[next_phase_index]
    scheduler.enter(next_delay, 1, publish_circadian_phase, argument=(next_phase, next_delay))


def run_circadian_rhythm_publisher() -> None:
    # Start publishing from the first phase
    initial_phase, initial_delay = CIRCADIAN_PHASES[0]
    scheduler.enter(0, 1, publish_circadian_phase, argument=(initial_phase, initial_delay))

    print('Starting circadian rhythm publisher...')
    scheduler.run()
