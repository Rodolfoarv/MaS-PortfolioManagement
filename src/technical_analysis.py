'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys
import time
from queries import query1

HOST = "127.0.0.1"

class TechnicalAnalysis(spade.Agent.Agent):
    def _setup(self):
        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RecvMsgBehav(),t)
        print "TechnicalAnalysis started!"



    class RecvMsgBehav(spade.Behaviour.OneShotBehaviour):

        def sendToAgent(self, perf, id, content):
         # Creamos el mensaje
         msg = spade.ACLMessage.ACLMessage()
         # Lo rellenamos
         msg.setOntology( "MaS" )
         msg.setPerformative( perf )
         msg.setConversationId( id )
         msg.setContent( '[{"Empresa": "Microsoft", "PrecioApertura": 114.31, "PrecioClausura": 114.06, "Pico": 114.56, "Depresion": 113.51, "Volumen": 24329900}, {"Empresa": "Apple", "PrecioApertura": 113.7, "PrecioClausura": 113.89, "Pico": 114.34, "Depresion": 113.13, "Volumen": 28779300}, {"Empresa": "Alphabet", "PrecioApertura": 113.4, "PrecioClausura": 113.05, "Pico": 113.66, "Depresion": 112.69, "Volumen": 21453100}, {"Empresa": "IBM", "PrecioApertura": 113.06, "PrecioClausura": 113.0, "Pico": 114.31, "Depresion": 112.63, "Volumen": 29736800}]' )

         receiver = spade.AID.aid(name="coordinator@"+HOST,
                                   addresses=["xmpp://coordinator@"+HOST])
         msg.addReceiver( receiver )
         print msg
         self._sendTo(msg, "coordinator@"+HOST)

        def onEnd(self):
            print "Closing agent.."
            self.myAgent._kill()

        def q1(self):
            print "Sleeping"
            time.sleep(5)
            self.sendToAgent("request", "result", "10,20,30,40")
            print "sent"



        def q2(self):
            return ""

        def _process(self):
            msg = self._receive(True)
            print "technical_analysis has received a message:"
            print str(msg.getContent())
            self.q1()


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
