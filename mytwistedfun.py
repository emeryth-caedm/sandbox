#!/usr/bin/python3

from twisted.internet import reactor, protocol, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


endpoints.serverFromString(reactor, "tcp:8000").listen(EchoFactory())
reactor.run()
