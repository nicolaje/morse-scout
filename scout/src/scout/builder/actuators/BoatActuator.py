from morse.builder.creator import ActuatorCreator

class Boatactuator(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "scout.actuators.BoatActuator.Boatactuator",\
                                 "BoatActuator")

