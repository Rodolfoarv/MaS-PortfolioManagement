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
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("TechnicalAnalysis")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.TechnicalAnalysisBehav(),mt)

    def sendToAgent(self, agent, performative, conversationID, content):
        msg = spade.ACLMessage.ACLMessage()
        msg.setOntology("MaS")
        msg.setPerformative(performative)
        msg.setConversationId(conversationID)
        msg.setContent(content)
        msg.addReceiver(spade.AID.aid(agent+"@"+HOST,["xmpp://"+ agent + "@" + HOST]))
        self.send(msg)


    class TechnicalAnalysisBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            self.q1()
            print "Waiting for response"
            self.msg = self._receive(True)
            print "Coordinator agent has received the response"
            print str(self.msg.getContent())

        #Query all share’s quotation on the current day
        def q1(self):
            content = "Apple, Alphabet, IBM, Microsoft"
            self.myAgent.sendToAgent("technical_analysis", "inform", "TechnicalAnalysis", content)


        #Query all share’s quotation on the current day
        def q2(self):
            pass

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
