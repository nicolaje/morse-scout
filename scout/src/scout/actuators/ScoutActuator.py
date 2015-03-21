import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.actuator

from morse.core.services import service, async_service, interruptible
from morse.core import status
from morse.helpers.components import add_data, add_property

class Scoutactuator(morse.core.actuator.Actuator):
    _name = "Scoutactuator"
    _short_desc = "Exposes the inputs of the scouts"

    add_data('u1', 0, 'double', 'Acceleration of the torpedo')
    add_data('u2', 0, 'double', 'Vertical orientation of the torpedo')
    add_data('u3', 0, 'double', 'Horizontal orientation of the torpedo')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        morse.core.actuator.Actuator.__init__(self, obj, parent)

        logger.info('Component initialized')

    def default_action(self):
        # Here you should make sure you pass self.local_data u1/u2/u3 to the scout...
        logger.info('ScoutActuator is not implemented')
        pass
