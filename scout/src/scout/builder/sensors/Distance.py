from morse.builder.creator import SensorCreator

class Distance(SensorCreator):
    def __init__(self, name=None):
        SensorCreator.__init__(self, name, \
                               "scout.sensors.Distance.Distance",\
                               "Distance")

