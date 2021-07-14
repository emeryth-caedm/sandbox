#!/usr/bin/python3

from twisted.internet import reactor,endpoints
from twisted.web.server import Site
from twisted.web.resource import Resource
import time

class ClockPage(Resource):
    isLeaf = True
    def render_GET(self, request):
        return (b"<!DOCTYPE html><html><head><meta charset='utf-8'>"
                b"<title>CLOCK!</title></head><body>" + time.ctime().encode('utf-8'))


resource = ClockPage()
factory = Site(resource)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(factory)
reactor.run()
