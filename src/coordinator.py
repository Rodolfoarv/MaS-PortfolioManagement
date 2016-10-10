# -*- coding: utf-8 -*-
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
        # Set the template for the Queries
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("request")
        template.setConversationId("q1")
        mt = spade.Behaviour.MessageTemplate(template)

        # Add Behaviour for Queries
    	self.addBehaviour(self.TechnicalAnalysis(), mt)
    	print "Sender started!"

    class TechnicalAnalysis(spade.Behaviour.OneShotBehaviour):

        #Query all share’s quotation on the current day
        def q1(self):
            print "test"
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+host,["xmpp://technical_analysis@"+host]))
            msg.setContent("SHARE ALL")
            self.myAgent.send(msg)

        #Query all share’s quotation on the current day
        def q2(self):
            print "test"
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+host,["xmpp://technical_analysis@"+host]))
            msg.setContent("SHARE ALL")
            self.myAgent.send(msg)

        def _process(self):
            self.q1()
            #Wait until the technical_analysis responds to us
            self.msg = self.receive(True)


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
