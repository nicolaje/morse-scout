import logging; logger = logging.getLogger("morse." + __name__)
import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS
from morse.core import blenderapi

class DistanceNotifier(AbstractMOOS):
    def default(self,  ci='unused'):
        cur_time=pymoos.MOOSCommClient.MOOSTime()
        # post the simulation time so that it can be synced to MOOSTime
        self.m.Notify('actual_time', blenderapi.persistantstorage().current_time, cur_time)
        for key, value in self.data['distances'].items():
            self.m.Notify(str(key), value, cur_time)
