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
import json
from datetime import datetime

from db.Queries import q01,q03,q04,q06,q07,q08


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
        self.addBehaviour(self.MonitorAbnormalTradingVolumeBehav(),mt)
        # self.addBehaviour(self.MonitorAbnormalTechnicalIndicator(),mt)
        print "\n\n*********** Monitor Agent has Started\n\n"


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

    class MonitorPriceFluctuationBehav(spade.Behaviour.Behaviour):
        '''Monitoring abnormal price fluctuation '''
        def _process(self):
            user_stocks = q01()
            # Obtain the stock information of every asset
            for stock in user_stocks:
                enterprise = stock['Empresa']
                current_date = datetime.now()
                date = current_date.strftime('%Y-%m-%d ')
                volumen = stock['Volumen']
                precio_apertura = stock['PrecioApertura']
                volatilidad = stock['Volatilidad']
                valor_actual = stock['ValorActual']
                precio_clausura = stock['PrecioClausura']
                currentPrice = valor_actual

                time.sleep(2)
                lastPrice = currentPrice
                randomPriceFluctuation = random.randint(-1000,1000)
                if randomPriceFluctuation > 900 or randomPriceFluctuation < -900:
                    currentPrice = currentPrice + randomPriceFluctuation
                    changePercentage = (currentPrice - lastPrice) / 100
                    print "******** Sending information to coordinator Abnormal Fluctuation detected!!!! ********"
                    content = {
                        'Enterprise' : enterprise,
                        'date' : date,
                        'lastPrice': lastPrice,
                        'currentPrice': currentPrice,
                        'changePercentage': changePercentage,
                    }
                    self.myAgent.sendToCoordinator("inform", "Monitor", content )
                else:
                    currentPrice = currentPrice + random.uniform(-20.3,40.0)
                    changePercentage = (currentPrice - lastPrice) / 100
                    content = {
                        'Enterprise' : enterprise,
                        'date' : date,
                        'lastPrice': lastPrice,
                        'currentPrice': currentPrice,
                        'changePercentage': changePercentage,
                    }
                #Update the database with the new values
                q08(currentPrice, enterprise)
                print "The current price for %s is: %f" %(enterprise,currentPrice)
                self.myAgent.sendToAgent("risk", "inform", "Monitor", content)
                self.myAgent.sendToAgent("decision_making", "inform", "Monitor", content)





    class MonitorAbnormalTradingVolumeBehav(spade.Behaviour.Behaviour):
        '''Monitoring abnormal trading volume '''
        def _process(self):
            print "Is this working?"
            user_stocks = q01()
            for stock in user_stocks:
                enterprise = stock['Empresa']
                current_date = datetime.now()
                date = current_date.strftime('%Y-%m-%d ')
                volumen = stock['Volumen']
                precio_apertura = stock['PrecioApertura']
                volatilidad = stock['Volatilidad']
                valor_actual = stock['ValorActual']
                precio_clausura = stock['PrecioClausura']
                currentPrice = valor_actual

                currentVolume = volumen
                time.sleep(2)
                lastVolume = currentVolume
                randomPriceFluctuation = random.randint(-1000,1000)
                if randomPriceFluctuation > 500 or randomPriceFluctuation < -500:
                    currentVolume = currentVolume + randomPriceFluctuation
                    print "*********** Sending information to coordinator Abnormal Volume detected!!!! ***********"
                    content = {
                        'Enterprise' : enterprise,
                        'date' : date,
                        'lastVolume': lastVolume,
                        'currentVolume': currentVolume,
                    }
                    self.myAgent.sendToCoordinator("inform", "Monitor", content )
                    break
                else:
                    currentVolume = currentVolume + random.randint(-20,40)

                print "The current volume for %s is: %d" %(enterprise,currentVolume)
                q07(currentVolume, enterprise)

    class MonitorAbnormalTechnicalIndicator(spade.Behaviour.Behaviour):
        '''Monitoring abnormal technical indicator's status'''
        def _process(self):
            user_interests = q04("aers@gmail.com")
            for stock in user_interests:
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
