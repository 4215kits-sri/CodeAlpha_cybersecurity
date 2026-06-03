from scapy.all import sniff
def process_packet(packet):
    print(packet.summary())

print("Starting Network Sniffer...")
sniff(prn=process_packet, count=10)