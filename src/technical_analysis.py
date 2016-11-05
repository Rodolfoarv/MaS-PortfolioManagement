'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys
import time
from queries import query1

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

    class RecvMsgBehav(spade.Behaviour.OneShotBehaviour):
        '''Class that will make the queries depending on the coordinator's request '''
        def _process(self):
            print "Waiting for message"
            self.msg = self._receive(True)
            print "technical_analysis has received a message:"
            print str(self.msg.getContent())
            print "Sending back the results to the Coordinator agent"
            self.q1()

        def q1(self):
            content = '[{"Empresa": "Microsoft", "PrecioApertura": 114.31, "PrecioClausura": 114.06, "Pico": 114.56, "Depresion": 113.51, "Volumen": 24329900}, {"Empresa": "Apple", "PrecioApertura": 113.7, "PrecioClausura": 113.89, "Pico": 114.34, "Depresion": 113.13, "Volumen": 28779300}, {"Empresa": "Alphabet", "PrecioApertura": 113.4, "PrecioClausura": 113.05, "Pico": 113.66, "Depresion": 112.69, "Volumen": 21453100}, {"Empresa": "IBM", "PrecioApertura": 113.06, "PrecioClausura": 113.0, "Pico": 114.31, "Depresion": 112.63, "Volumen": 29736800}]'
            self.myAgent.sendToCoordinator("request", "TechnicalAnalysis", content )

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
