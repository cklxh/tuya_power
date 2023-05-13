"""The tuya_power component."""
import logging

from homeassistant.const import STATE_UNKNOWN
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DOMAIN = "tuya_power"

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the tuya_power platform."""
    add_entities([TuyaPower(config["entity_id"])])

class TuyaPower(Entity):
    """Representation of a Sensor."""

    def __init__(self, entity_id):
        """Initialize the sensor."""
        self._state = STATE_UNKNOWN
        self.entity_id = entity_id

    @property
    def name(self):
        """Return the name of the sensor."""
        return "My Sensor"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        self._state = self.hass.states.get(self.entity_id).state
