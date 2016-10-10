import spade
HOST = "127.0.0.1"

class Receiver(spade.Agent.Agent):

    class RecvMsgBehav(spade.Behaviour.OneShotBehaviour):

        def _process(self):
            msg = self._receive(block=True,timeout=10)
            print "b has received a message:"
            print str(msg)

    def _setup(self):

        template = spade.Behaviour.ACLTemplate()
        template.setSender(spade.AID.aid("a@"+HOST,["xmpp://a@"+HOST]))
        t = spade.Behaviour.MessageTemplate(template)
        self.addBehaviour(self.RecvMsgBehav(),t)
	print "Receiver started!"



if __name__ == "__main__":
	b = Receiver("b@"+HOST,"secret")
	b.start()
        alive = True
        import time
        while alive:
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                alive=False
        b.stop()
        sys.exit(0)
