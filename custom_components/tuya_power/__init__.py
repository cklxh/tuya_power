"""
Example custom integration for Home Assistant.

For more details about this integration, please refer to the documentation at
https://github.com/home-assistant/example-custom-config/tree/master/custom_components/my_custom_integration
"""

DOMAIN = "tuya_power"

async def async_setup(hass, config):
    """Set up the My Custom Integration component."""
    # This method gets called when the integration is loaded. You can use it
    # to set up any global state, or load any other dependencies.
    return True
