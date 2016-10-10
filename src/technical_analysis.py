'''
Coordinator Agent description, receiver to their agents
'''

import spade
import sys

HOST = "127.0.0.1"

class TechnicalAnalysis(spade.Agent.Agent):

    class RecvMsgBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = self._receive(block=True,timeout=10)
            print "technical_analysis has received a message:"
            print str(msg)

    def _setup(self):

        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("coordinator@"+HOST,["xmpp://coordinator@"+HOST]))
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RecvMsgBehav(),t)
	print "TechnicalAnalysis started!"



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
