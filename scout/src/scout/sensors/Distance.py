import logging; logger = logging.getLogger("morse." + __name__)

import morse.core.sensor

from morse.core import blenderapi
from morse.core.services import service, async_service
from morse.core import status
from morse.helpers.components import add_data, add_property

class Distance(morse.core.sensor.Sensor):
    _name = "Distance"
    _short_desc = "Measure the distances to all the robots in the scene"

    # define here the data fields exported by your sensor
    # format is: field name, default initial value, type, description
    add_data('distances', {}, 'dict', 'All the distances to all the robots in the scene')

    def __init__(self, obj, parent=None):
        logger.info("%s initialization" % obj.name)
        # Call the constructor of the parent class
        morse.core.sensor.Sensor.__init__(self, obj, parent)
        logger.info('Component initialized')

    def default_action(self):
        self.local_data['distances']={} # empty the dict
        parent = self.robot_parent.bge_object
        # Loop through all the objects in the scene
        for obj in blenderapi.scene().objects:
          # Skip distance to self
          if parent != obj:
            distance = self._measure_distance_to_object (parent, obj)
            self.local_data['distances'][obj.name] = distance

    def _measure_distance_to_object(self, own_robot, target_object):
        distance, globalVector, localVector = own_robot.getVectTo(target_object)
        return distance
