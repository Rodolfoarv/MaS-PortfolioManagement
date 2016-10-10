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
        #Set the template for QueryAllShares
        templateQ1 = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("request")
        template.setConversationId("q1")
        mt = spade.Behaviour.MessageTemplate(template)

        #Add Behaviour for Query 1 - Query all share’s quotation on the current day
		self.addBehaviour(self.QueryAllShares(), mt)

        #Add Behaviour for Query 2 - Query a given share’s quotation on the current day
        template.setPerformative("request")
        template.setConversationId("q2")

        self.addBehaviour(self.QueryGivenShare())
		print "Sender started!"

    class QueryAllShares(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+host,["xmpp://technical_analysis@"+host]))
            msg.setContent("SHARE ALL")
            self.myAgent.send(msg)

            print "coordinator has sent coordinator message:"
            print str(msg)

    class QueryGivenShare(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+host,["xmpp://technical_analysis@"+host]))
            msg.setContent("SHARE ONE")

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
