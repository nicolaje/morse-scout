from morse.builder import *

class Boat(GroundRobot):
    """
    A template robot model for Boat, with a motion controller and a pose sensor.
    """
    def __init__(self, name = None, debug = True):
        # Boat.blend is located in the data/robots directory
        GroundRobot.__init__(self, 'scout/robots/Boat.blend', name)
        self.properties(classpath = "scout.robots.Boat.Boat")
