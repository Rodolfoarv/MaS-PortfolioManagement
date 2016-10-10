'''
Coordinator Agent description, send messages to their agents
'''

import os
import sys
import time
import unittest
import spade

host = "127.0.0.1"

class Coordinator(spade.Agent.Agent):

    def _setup(self):
		self.addBehaviour(self.SendMsgBehav())
		print "Sender started!"

    class SendMsgBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("inform")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+host,["xmpp://technical_analysis@"+host]))
            msg.setContent("testSendMsg")

            self.myAgent.send(msg)

            print "coordinator has sent coordinator message:"
            print str(msg)


if __name__ == "__main__":
	coordinator = Coordinator("coordinator@"+host,"secret")
	coordinator.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        coordinator.stop()
        sys.exit(0)
