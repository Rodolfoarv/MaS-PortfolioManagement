# -*- coding: utf-8 -*-
'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys
import time
from db.Queries import q01,q02,q03,q10

HOST = "127.0.0.1"

class TechnicalAnalysis(spade.Agent.Agent):
    '''The technical analysis agent (TAA) retrieves and processes
    the raw stock trading data from the Internet, stores the raw
    data to a relevant database (HTDB, RTDB), calculates various
    technical indicators, identifies various price and trading
    volume patterns, and gives the output to the DMA.  '''

    def _setup(self):
        '''Initial setup for the technical analysis, it will query what the coordinator asks for '''
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("request")
        template.setConversationId("TechnicalAnalysis")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RecvMsgBehav(),mt)

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

    class RecvMsgBehav(spade.Behaviour.Behaviour):
        '''Class that will make the queries depending on the coordinator's request '''
        def _process(self):
            print "Waiting for query request"
            self.msg = self._receive(True)
            content = self.msg.getContent()
            content = content.split()
            print "Sending back the results to the Coordinator agent"

            if content[0] == "q01":
                self.q1()
            elif content[0] == "q02":
                enterprise = content[1]
                self.q2(enterprise)
            elif content[0] == "q03":
                email = content[1]
                self.q3(email)
            elif content[0] == "q10":
                email = content[1]
                self.q10(email)

        def q1(self):
            content = q01()
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )

        #Query a given share’s quotation on the current day
        def q2(self, enterprise):
            ''' Query a given share's quotation on the current day '''
            content = q02(enterprise)
            print content
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )

        # Query all stock from today's related with my preferneces
        def q3(self,email):
            '''Query all stock from today's related with my preferneces'''
            content = q03(email)
            print content
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )

        # Query a given share’s history price chart over a period
        def q4(self, enterprise, startDate, endDate):
            '''Query a given share's history price chart over a period'''
            pass

        # Query a given share's price and technical indicator chart over a period
        def q5(self):
            ''' Query a given share's price and technical indicator chart over a period'''
            content = q05(enterprise,startDate,endDate)
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )
            pass

        # Query a given share’s fundamental analysis data
        def q6(self):
            ''' Query a given share's fundamental analysis data '''
            pass

        # Query the market statistic information over a period
        def q7(self):
            ''' Query the market statistic information over a period '''
            pass

        def q10(self,email):
            ''' Query all stocks I have inversions in '''
            content = q10(email)
            print content
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )






if __name__ == "__main__":
	technical_analysis = TechnicalAnalysis("technical_analysis@"+HOST,"secret")
	technical_analysis.start()
        alive = True
        import time
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        technical_analysis.stop()
        sys.exit(0)
