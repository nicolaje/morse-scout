import logging; logger = logging.getLogger("morse." + __name__)
import morse.core.robot

class Scout(morse.core.robot.Robot):
    _name = 'Scout robot'

    # speed
    _v = 0

    _u1 = 0
    _u2 = 0
    _u3 = 0

    def __init__(self, obj, parent=None):
        logger.info('%s initialization' % obj.name)
        morse.core.robot.Robot.__init__(self, obj, parent)

    def default_action(self):
        # Here you should make sure you integrate the state equations of the scout
        logger.info('Scout state equations are not implemented')
        self.bge_object.applyMovement([0, 0, 0])
        pass
