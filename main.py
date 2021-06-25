from scapy.all import *

ether = Ether(src='04:92:26:D7:EC:AC', dst='ff:ff:ff:ff:ff:ff')
ip = IP(src='0.0.0.0', dst='255.255.255.255')
udp = UDP(sport=68, dport=67)
bootp = BOOTP()
dhcp = DHCP(options=[('message-type', 'inform'), 'end'])
packet = ether / ip / udp / bootp / dhcp

packet.show()

sendp(packet, verbose=2)
