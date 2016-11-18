#!/usr/local/env python3
import subprocess
import matplotlib.pyplot as plt
import time

class pyPinger:
    def __init__(self, domain, times):
        self.domain = str(domain)
        self.times = int(times)

    def process(self):

        print("[Message] Pinging %s ..." % self.domain)
        date = str(time.strftime("%Y-%m-%d_%H.%M.%S"))
        theCommand = "ping %s -c%d" % (self.domain, self.times)
        proc = subprocess.Popen(theCommand, shell=True, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        output = output.decode('utf-8')

        theArray = []
        for i in range(1, self.times+1):
            timeAt = output.split("\n")[i].find("time")
            theTime = output.split("\n")[i][timeAt:]
            theEqual = theTime.find("=")
            theMs = theTime[theEqual+1:]
            theMs = float(theMs.split(" ")[0])
            theArray.append(theMs)

        print(theArray)
        plt.plot(theArray)

        plt.savefig("%s_%s.png" % (self.domain, date), dpi=72, format="png")


if __name__ == '__main__':

    domain = pyPinger("www.google.com.tw", 10)
    domain.process()
