import logging; logger = logging.getLogger("morse." + __name__)
import pymoos.MOOSCommClient
from morse.middleware.moos import AbstractMOOS

class ScoutActuatorReader(AbstractMOOS):
    def initialize(self):
        AbstractMOOS.initialize(self)

        # register for control variables from the database
        self.m.Register("u1")
        self.m.Register("u2")
        self.m.Register("u3")

    def default(self, ci='unused'):
        current_time = pymoos.MOOSCommClient.MOOSTime()
        # get latest mail from the MOOS comm client
        messages = self.m.FetchRecentMail()

        # look for command messages: u1 and u2
        for message in messages:
            if (message.GetKey() =="u1") and (message.IsDouble()):
                self.data['u1'] = message.GetDouble() # command linear acceleration
            elif  (message.GetKey()=="u2") and (message.IsDouble()):
                self.data['u2'] = message.GetDouble() # command angular rudder vertical
            elif  (message.GetKey()=="u3") and (message.IsDouble()):
                self.data['u3'] = message.GetDouble() # command angular rudder horizontal
