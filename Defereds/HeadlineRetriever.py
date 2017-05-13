from twisted.internet import reactor,defer

class HeadlineRetriever(object):
    def processHeadline(self,headline):
        print("processHeadline")
        if len(headline)>50:
            self.d.errback(ValueError("The headline %s is too long"%(headline)))
        else:
            self.d.callback(headline)

    def toHTML(self,result):
        print("toHTML")
        return "<H1>%s</H1>" %(result)

    def getHeadline(self,input):
        print("getHeadline")
        self.d = defer.Deferred()
        reactor.callLater(1,self.processHeadline,input) # asking the reactor to schedule processHeadline
                                                        # in 1 seconds time with the result input
        self.d.addCallback(self.toHTML)
        return self.d

def printData(result):
    print(result)
    reactor.stop()

def printError(failure):
    print(failure)
    reactor.stop()

h = HeadlineRetriever()
d = h.getHeadline("111111111111111111111111Breaking News: Twisted Takes Us to the Moon!")
d.addCallbacks(printData,printError)
reactor.run()
