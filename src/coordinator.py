# -*- coding: utf-8 -*-
'''
Coordinator Agent description, send messages to their agents
'''

import os
import sys
import time
import unittest
import spade

HOST = "127.0.0.1"

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

        #Add Behaviour for results
        template.setConversationId("result")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.Result(),mt)



    class TechnicalAnalysis(spade.Behaviour.OneShotBehaviour):

        def onEnd(self):
            print "Closing agent.."
            self.myAgent._kill()

        #Query all share’s quotation on the current day
        def q1(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+HOST,["xmpp://technical_analysis@"+HOST]))
            msg.setContent("SHARE ALL")
            self.myAgent.send(msg)

        #Query all share’s quotation on the current day
        def q2(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setPerformative("request")
            msg.addReceiver(spade.AID.aid("technical_analysis@"+HOST,["xmpp://technical_analysis@"+HOST]))
            msg.setContent("SHARE ALL")
            self.myAgent.send(msg)

        # Query a given share’s real-time trading chart
        def q3(self):
            pass

        # Query a given share’s history price chart over a period
        def q4(self):
            pass

        # Query a given share's price and technical indicator chart over a period
        def q5(self):
            pass

        # Query a given share’s fundamental analysis data
        def q6(self):
            pass

        # Query the market statistic information over a period
        def q7(self):
            pass

        def _process(self):
            self.q1()

    class Result(spade.Behaviour.OneShotBehaviour):
        def _process(self):
            #Wait until the technical_analysis responds to us
            print "Waiting for response"
            self.msg = self._receive(True,10)
            print self.msg



if __name__ == "__main__":
	coordinator = Coordinator("coordinator@"+HOST,"secret")
	coordinator.start()

        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        print "Coordinator stopped"
        coordinator.stop()
        sys.exit(0)
