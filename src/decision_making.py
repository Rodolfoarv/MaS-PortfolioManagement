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
historic_prices = {}
historic_volumes = {}

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
        template.setConversationId("Decision")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.DecisionBehav(),mt)

        for stock in q01():
            enterprise = stock['Empresa']
            historic_prices[enterprise] = []
            historic_volumes[enterprise] = []
            historic_prices[enterprise].append(stock['ValorActual'])
            historic_volumes[enterprise].append(stock['Volumen'])


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

    class DecisionBehav(spade.Behaviour.Behaviour):
        def strategy1(self,enterprise, historic_prices ):
            """The value of the stock goes up 2 times then report to sell"""
            subArray = historic_prices[0:3]
            length = len(subArray)
            for i in range(length):
                if subArray[0] > subArray[1] and subArray[1] > subArray[2]:
                    content = "You should sell the auction %s due to the Strategy #1: If it goes up 2 times then sell" %(enterprise)
                    self.myAgent.sendToCoordinator("inform", "Decision", content )

        def strategy2(self,enterprise,historic_prices):
            """The value of the stock goes down 5 times in row"""
            subArray = historic_prices[0:6]
            length = len(subArray)
            for i in range(length):
                if subArray[0] < subArray[1] and subArray[1] < subArray[2] and subArray[2] < subArray[3] and subArray[3] < subArray[4] and subArray[4] < subArray[5]:
                    content = "You should sell the auction %s due to the Strategy #2: The value of the stock went up 5 times" %(enterprise)
                    self.myAgent.sendToCoordinator("inform", "Decision", content )

        def strategy3(self,enterprise,historic_prices):
            """If the value of an auction volume has an abnormal positive change, then buy"""
            subArray = historic_prices[0:2]
            if (subArray[0] - subArray[1]) > 5000:
                content = "You should buy the auction %s due to the Strategy #3: The volume of the auction has changed" %(enterprise)
                self.myAgent.sendToCoordinator("inform", "Decision", content )





        def _process(self):
            #Wait for a message from the monitor agent
            time.sleep(1)

            for stock in q01():
                enterprise = stock['Empresa']
                if len(historic_prices[enterprise]) > 10:
                    historic_prices[enterprise] = []
                    historic_volumes[enterprise] = []
                historic_prices[enterprise].insert(0,stock['ValorActual'])
                historic_volumes[enterprise].insert(0,stock['Volumen'])
                currentPrice = 0
                lastPrice = 0
                print historic_volumes

                # Strategy 1, If the value of my auction goes up 2 times
                if len(historic_prices[enterprise]) > 2:
                    self.strategy1(enterprise,historic_prices[enterprise])

                if len(historic_prices[enterprise]) > 5:
                    self.strategy2(enterprise,historic_prices[enterprise])






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
