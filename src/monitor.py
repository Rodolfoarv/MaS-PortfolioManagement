# -*- coding: utf-8 -*-
'''
Monitor agent which will be in charge to do the following tasks:
    • MA1 — Monitoring abnormal price fluctuation
    • MA2 — Monitoring abnormal trading volume
    • MA3 — Monitoring abnormal technical indicator’s status
    • MA4 — Monitoring abnormal price chart pattern
    * MA5 — Monitoring breaking news relating to the given shares
'''

import os
import sys
import time
import unittest
import spade

HOST = "127.0.0.1"

class Coordinator(spade.Agent.Agent):
    '''The monitoring agent monitors the status of
    the given stocks on behalf of users according
    to their profiles. This agent reports on the
    technical indicators status of the given stocks
    and notifies any abnormal changes in trading
    volume and price  '''

    def _setup(self):
        ''' Initial setup for the Coordinator it will addBehaviour for the
        different agents that the simulation will use'''

        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("Monitor")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.TechnicalAnalysisBehav(),mt)

    def sendToAgent(self, agent, performative, conversationID, content):
        ''' Method that takes as arguments the agent name, performative, conversationID
        and content to be sent to any agent'''

        msg = spade.ACLMessage.ACLMessage()
        msg.setOntology("MaS")
        msg.setPerformative(performative)
        msg.setConversationId(conversationID)
        msg.setContent(content)
        msg.addReceiver(spade.AID.aid(agent+"@"+HOST,["xmpp://"+ agent + "@" + HOST]))
        self.send(msg)
