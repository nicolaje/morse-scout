import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot

class Boat(morse.core.robot.Robot):
    _name = 'Boat robot'

    # Speed
    _v = 0
    
    # u1 (acceleration)
    _u1 = 0
    # u2 (rudder)
    _u2 = 0

    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)

    def default_action(self):
        # Integrate the state - equations of the boat here
        logger.info('Boat state equations are not implemented')
        self.bge_object.applyMovement([0, 0, 0])
        pass
