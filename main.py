"""
CodeAlpha Internship - Task 1: Basic Network Sniffer
Use only on devices and networks you own or have explicit permission to monitor.
Run from an Administrator terminal on Windows with Npcap installed.
"""
from datetime import datetime
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def analyze_packet(packet):
    print("\n" + "=" * 60)
    print("              BASIC NETWORK SNIFFER")
    print("=" * 60)
    print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if not packet.haslayer(IP):
        print("Non-IPv4 packet:", packet.summary())
        return

    ip_layer = packet[IP]
    print("Source IP       :", ip_layer.src)
    print("Destination IP  :", ip_layer.dst)
    print("IP Version      :", ip_layer.version)
    print("Packet Size     :", len(packet), "bytes")

    if packet.haslayer(TCP):
        print("Protocol        : TCP")
        print("Source Port     :", packet[TCP].sport)
        print("Destination Port:", packet[TCP].dport)
    elif packet.haslayer(UDP):
        print("Protocol        : UDP")
        print("Source Port     :", packet[UDP].sport)
        print("Destination Port:", packet[UDP].dport)
    elif packet.haslayer(ICMP):
        print("Protocol        : ICMP")
    else:
        print("IP Protocol No. :", ip_layer.proto)

    # Show only a short hex preview rather than dumping full payload contents.
    if packet.haslayer(Raw):
        payload = bytes(packet[Raw].load)
        print("Payload Length  :", len(payload), "bytes")
        print("Payload Preview :", payload[:80].hex(" "))


def start_sniffer():
    print("=" * 60)
    print("       CODEALPHA - BASIC NETWORK SNIFFER")
    print("=" * 60)
    print("Starting packet capture...")
    print("Press CTRL+C to stop.")

    try:
        sniff(prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
    except PermissionError:
        print("\nPermission denied. Reopen your terminal as Administrator.")
    except Exception as error:
        print(f"\nCapture error: {error}")
        print("Check Npcap installation and available capture interfaces.")


if __name__ == "__main__":
    start_sniffer()
