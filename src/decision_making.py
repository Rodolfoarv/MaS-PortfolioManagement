# -*- coding: utf-8 -*-
'''
Decision Making Agent which will be in charge of supporting the decision
the user should make with respect of his stocks, i.e buying, holding or selling
their shares
'''

import os
import sys
import time
import unittest
import spade
import random
import json

from db.Queries import q01,q03,q04,q06


HOST = "127.0.0.1"

class DecisionMaking(spade.Agent.Agent):
    '''The decision making agent is in charge
    on helping the user to make his decisions
    for buying, selling or holding shares depending
    on what the user has specified previously '''

    def _setup(self):
        ''''''
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("Monitor")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.SellingRuleBehav(),mt)
        print "\n\n*********** Decision Making Agent has Started\n\n"


    def sendToCoordinator(self, performative, conversationID, content):
        '''Function that takes as parameter the perfomative, conversation and content to
        be sent back to the coordinator '''
        msg = spade.ACLMessage.ACLMessage()
        msg.setOntology("MaS")
        msg.setPerformative(performative)
        msg.setConversationId(conversationID)
        msg.setContent(content)
        msg.addReceiver(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
        print "Sending....."
        self.send(msg)

    class SellingRuleBehav(spade.Behaviour.Behaviour):
        def _process(self):
            #Wait for a message from the monitor agent
            self.msg = self._receive(True)
            print str(self.msg.getContent())






if __name__ == "__main__":
	decision_making = DecisionMaking("decision_making@"+HOST,"secret")
	decision_making.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        print "Decision Making stopped"
        decision_making.stop()
        sys.exit(0)
