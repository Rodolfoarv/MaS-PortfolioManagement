import os
import sys
import time
import unittest
import spade
import random
import json
import ast

from datetime import datetime

from db.Queries import q01,q03,q04,q06

HOST = "127.0.0.1"

user_stocks = q01()
empresasRiesgos = []
for stock in user_stocks:
    #print stock
    enterprise = stock['Empresa']
    risksValues = []
    lastPrice = stock['ValorActual']
    enterpriseRisk = {
        'Enterprise' : enterprise,
        'RisksValues' : risksValues,
        'LastPrice' : lastPrice,
    }
    empresasRiesgos.append(enterpriseRisk)

class Risk(spade.Agent.Agent):

    def _setup(self):
        ''''''
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("Risk")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RiskAnalysisBehav(),mt)

        print "\n\n*********** Risk Agent has Started\n\n"

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

    class RiskAnalysisBehav(spade.Behaviour.Behaviour):
        def _process(self):
            time.sleep(2)
            for stock in q01():
                #print stock
                #print stock['Empresa']
                #print empresasRiesgos
                for stock2 in empresasRiesgos:
                    #print stock['Empresa']
                    #print stock2['Enterprise']
                    if stock['Empresa'] == stock2['Enterprise']:
                        print stock['ValorActual']
                        changePercentage = (stock['ValorActual'] - stock2['LastPrice']) / 100
                        stock2['LastPrice'] = stock['ValorActual']
                        if len(stock2['RisksValues']) >= 15:
                            stock2['RisksValues'].pop(0)
                            stock2['RisksValues'].append(changePercentage)
                        else:
                            stock2['RisksValues'].append(changePercentage)
                        print "Historic Risks of %s:" %stock2['Enterprise']
                        print stock2['RisksValues']
                        totalRisk = 0   
                        for risk in stock2['RisksValues']:
                            totalRisk += risk
                            #print totalRisk
                        print "totalRisk: %s" %totalRisk
                        if totalRisk <= -7:
                            print '***********Notificar a gente de toma de decisiones*******************'
                            stock2['RisksValues'] = []
                        

if __name__ == "__main__":
	risk = Risk("risk@"+HOST,"secret")
	risk.start()
        alive = True
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        print "Risk stopped"
        risk.stop()
        sys.exit(0)
