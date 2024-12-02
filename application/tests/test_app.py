from application.app import app


def test_flask_app_initialization():
    """Test if Flask app initializes correctly."""
    assert app is not None
    assert app.config['MQTT_BROKER_URL'] is not None
