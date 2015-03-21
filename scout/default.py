#! /usr/bin/env morseexec

from morse.builder import *
from scout.builder.robots import Boat
from scout.builder.actuators import Boatactuator

from scout.builder.robots import Scout
from scout.builder.actuators import Scoutactuator

from scout.builder.sensors import Distance

boat = Boat()

BoatActuator = Boatactuator()
BoatActuator.add_stream('moos','scout.actuators.boatActuatorReader.BoatActuatorReader',moos_port=9000)

Distance1 = Distance()
Distance1.add_stream('moos','scout.sensors.distanceNotifier.DistanceNotifier', moos_port=9000)

boat.append(BoatActuator)
boat.append(Distance1)

scout1 = Scout()

ScoutActuator1 = Scoutactuator()
ScoutActuator1.add_stream('moos','scout.actuators.scoutActuatorReader.ScoutActuatorReader',moos_port=9001)

Distance2 = Distance()
Distance2.add_stream('moos','scout.sensors.distanceNotifier.DistanceNotifier', moos_port=9001)

scout1.append(ScoutActuator1)
scout1.append(Distance2)

scout2 = Scout()

ScoutActuator2 = Scoutactuator()
ScoutActuator2.add_stream('moos','scout.actuators.scoutActuatorReader.ScoutActuatorReader',moos_port=9002)

Distance3 = Distance()
Distance3.add_stream('moos','scout.sensors.distanceNotifier.DistanceNotifier', moos_port=9002)

scout2.append(ScoutActuator2)
scout2.append(Distance3)

scout1.translate(10,-5,0)
scout2.translate(10,5,0)

# set 'fastmode' to True to switch to wireframe mode
env = Environment('water-1/deep_water', fastmode = False)
env.set_camera_location([10.0, -10.0, 10.0])
env.set_camera_rotation([1.05, 0, 0.78])

