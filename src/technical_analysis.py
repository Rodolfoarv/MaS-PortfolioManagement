'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys
import time

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
         msg.setContent( content )

         receiver = spade.AID.aid(name="coordinator@"+HOST,
                                   addresses=["xmpp://coordinator@"+HOST])
         msg.addReceiver( receiver )
         print msg
         self._sendTo(msg, "coordinator@"+HOST)
         print "done"

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
