from morse.builder.creator import ActuatorCreator

class Scoutactuator(ActuatorCreator):
    def __init__(self, name=None):
        ActuatorCreator.__init__(self, name, \
                                 "scout.actuators.ScoutActuator.Scoutactuator",\
                                 "ScoutActuator")

