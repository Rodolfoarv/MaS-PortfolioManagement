'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys
import time
from queries import query1

HOST = "127.0.0.1"

class TechnicalAnalysis(spade.Agent.Agent):
# template.setSender(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
    def _setup(self):
        template = spade.Behaviour.ACLTemplate()
        template.setOntology("MaS")
        template.setPerformative("inform")
        template.setConversationId("TechnicalAnalysis")
        mt = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RecvMsgBehav(),mt)

    def sendToCoordinator(self, perf, id, content):
        msg = spade.ACLMessage.ACLMessage()
        msg.setOntology("MaS")
        msg.setPerformative("inform")
        msg.setConversationId("TechnicalAnalysis")
        msg.setContent( '[{"Empresa": "Microsoft", "PrecioApertura": 114.31, "PrecioClausura": 114.06, "Pico": 114.56, "Depresion": 113.51, "Volumen": 24329900}, {"Empresa": "Apple", "PrecioApertura": 113.7, "PrecioClausura": 113.89, "Pico": 114.34, "Depresion": 113.13, "Volumen": 28779300}, {"Empresa": "Alphabet", "PrecioApertura": 113.4, "PrecioClausura": 113.05, "Pico": 113.66, "Depresion": 112.69, "Volumen": 21453100}, {"Empresa": "IBM", "PrecioApertura": 113.06, "PrecioClausura": 113.0, "Pico": 114.31, "Depresion": 112.63, "Volumen": 29736800}]' )
        msg.addReceiver(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
        self.myAgent.send(msg)
        print msg

    class RecvMsgBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            print "Waiting for message"
            self.msg = self._receive(True)
            print "technical_analysis has received a message:"
            print str(self.msg.getContent())
            print "Sending back the results to the Coordinator agent"
            self.q1()


        def q1(self):
            msg = spade.ACLMessage.ACLMessage()
            msg.setOntology("MaS")
            msg.setPerformative("inform")
            msg.setConversationId("TechnicalAnalysis")
            msg.setContent( '[{"Empresa": "Microsoft", "PrecioApertura": 114.31, "PrecioClausura": 114.06, "Pico": 114.56, "Depresion": 113.51, "Volumen": 24329900}, {"Empresa": "Apple", "PrecioApertura": 113.7, "PrecioClausura": 113.89, "Pico": 114.34, "Depresion": 113.13, "Volumen": 28779300}, {"Empresa": "Alphabet", "PrecioApertura": 113.4, "PrecioClausura": 113.05, "Pico": 113.66, "Depresion": 112.69, "Volumen": 21453100}, {"Empresa": "IBM", "PrecioApertura": 113.06, "PrecioClausura": 113.0, "Pico": 114.31, "Depresion": 112.63, "Volumen": 29736800}]' )
            msg.addReceiver(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
            print "Sending....."
            self.myAgent.send(msg)


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
