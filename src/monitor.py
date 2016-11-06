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
import random

HOST = "127.0.0.1"

class Monitor(spade.Agent.Agent):
    '''The monitoring agent monitors the status of
    the given stocks on behalf of users according
    to their profiles. This agent reports on the
    technical indicators status of the given stocks
    and notifies any abnormal changes in trading
    volume and price  '''

    def _setup(self):
        ''''''

        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("Monitor")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.MonitorPriceFluctuationBehav(),mt)

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

    class MonitorPriceFluctuationBehav(spade.Behaviour.Behaviour):
        '''Monitoring abnormal price fluctuation '''
        def _process(self):
            print "Starting Abnormal price fluctuation"
            date = "Nov 04, 2016"
            price = 100
            while True:
                time.sleep(2)
                lastPrice = price
                randomPriceFluctuation = random.randint(-1000,1000)
                if randomPriceFluctuation > 900 or randomPriceFluctuation < -900:
                    print "randomPriceFluctuation"
                    price = price + randomPriceFluctuation
                    changePercentage = (price - lastPrice) / 100
                    print "Sending information to coordinator Random Fluctuation detected!!!!"
                    content = "Last Price: " + str(lastPrice)+ " Price:" +  str(price) +  " Change Percentage: " + str(changePercentage)
                    self.myAgent.sendToCoordinator("inform", "Monitor", content )
                    break
                else:
                    price = price + random.uniform(-20.3,40.0)
                    print price


    class MonitorAbnormalTradingVolume(spade.Behaviour.Behaviour):
        '''  '''
        def _process(self):
            pass


if __name__ == "__main__":
	monitor = Monitor("monitor@"+HOST,"secret")
	monitor.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        print "Monitor stopped"
        monitor.stop()
        sys.exit(0)
