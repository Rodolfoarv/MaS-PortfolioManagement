##################################
#   SEND AND RECEIVE             #
##################################
'''
This is the most simple example about how
to send a message between 2 agents
'''

import os
import sys
import time
import unittest

sys.path.append('../..')

import spade

host = "127.0.0.1"


class Sender(spade.Agent.Agent):

    def _setup(self):
		self.addBehaviour(self.SendMsgBehav())
		print "Sender started!"

    class SendMsgBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("b@"+host,["xmpp://b@"+host]))
            msg.setContent("testSendMsg")

            self.myAgent.send(msg)

            print "a has sent a message:"
            print str(msg)

if __name__ == "__main__":
	a = Sender("a@"+host,"secret")
	a.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        a.stop()
        sys.exit(0)
