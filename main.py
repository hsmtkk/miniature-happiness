from scapy.all import *

ether = Ether(src='08:00:27:4A:50:63', dst='08:00:27:a2:86:76')
ip = IP(src='10.1.1.100', dst='10.1.1.1')
udp = UDP(sport=68, dport=67)
bootp = BOOTP()
dhcp = DHCP(options=[('message-type', 'inform'), 'end'])
packet = ether / ip / udp / bootp / dhcp

packet.show()

sendp(packet, verbose=2)
