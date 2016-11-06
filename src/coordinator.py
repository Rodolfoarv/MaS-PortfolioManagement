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
    '''The coordinator agent (CA) is responsible for
    task decomposition and planning. The CA
    maintains a set of beliefs about the capabilities
    of all agents in MASST. It can decompose a
    given task into a number of subtasks and dispatch
    the subtasks to relevant agents to execution,
    in order to achieve its goals. '''

    def _setup(self):
        ''' Initial setup for the Coordinator it will addBehaviour for the
        different agents that the simulation will use'''

        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("request")
        template.setConversationId("TechnicalAnalysis")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.TechnicalAnalysisBehav(),mt)

        # Add the monitor agent
        template.setPerformative("inform")
        template.setConversationId("Monitor")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.MonitorBehav(),mt)



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

    class TechnicalAnalysisBehav(spade.Behaviour.Behaviour):
        ''' Behavior that will simulate the interaction between the Technical Analysis
        agent, it will query what it needs, such as retrieving information from a specific date,
        a given share, a range between dates, etc '''

        def _process(self):
            self.q1()
            print "Waiting for response"
            self.msg = self._receive(True)
            print "Coordinator agent has received the response"
            print str(self.msg.getContent())

        #Query all share’s quotation on the current day
        def q1(self):
            ''' Query all share's quotation on the current day '''

            content = "Apple, Alphabet, IBM, Microsoft"
            self.myAgent.sendToAgent("technical_analysis", "request", "TechnicalAnalysis", content)

        #Query a given share’s quotation on the current day
        def q2(self):
            ''' Query a given share's quotation on the current day '''
            pass

        # Query a given share’s real-time trading chart
        def q3(self):
            '''Query a given share's real time trading chart'''
            pass

        # Query a given share’s history price chart over a period
        def q4(self):
            '''Query a given share's history price chart over a period'''
            pass

        # Query a given share's price and technical indicator chart over a period
        def q5(self):
            ''' Query a given share's price and technical indicator chart over a period'''
            pass

        # Query a given share’s fundamental analysis data
        def q6(self):
            ''' Query a given share's fundamental analysis data '''
            pass

        # Query the market statistic information over a period
        def q7(self):
            ''' Query the market statistic information over a period '''
            pass

    class MonitorBehav(spade.Behaviour.Behaviour):
        def _process(self):
            print "Waiting for response from the monitor agent"
            self.msg = self._receive(True)
            print "Coordinator agent has received the response"
            print str(self.msg.getContent())

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
