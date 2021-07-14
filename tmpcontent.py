#!/usr/bin/python3

from twisted.web.server import Site
from twisted.web.static import File
from twisted.internet import reactor, endpoints

resource = File("/tmp")
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8000)
endpoint.listen(factory)
reactor.run()