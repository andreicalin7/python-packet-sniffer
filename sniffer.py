from colorama import Fore
from scapy.layers.inet import IP, TCP, UDP

from config import FILTER_PROTOCOL
from logger import log_packet

# Counters
packet_count = 0
tcp_count = 0
udp_count = 0


def packet_callback(packet):
    global packet_count, tcp_count, udp_count

    if not packet.haslayer(IP):
        return

    packet_count += 1

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst

    if FILTER_PROTOCOL == "TCP" and packet.haslayer(TCP):
        tcp_count += 1

        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        message = f"[TCP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
        print(Fore.GREEN + message)
        log_packet(message)

    elif FILTER_PROTOCOL == "UDP" and packet.haslayer(UDP):
        udp_count += 1

        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport

        message = f"[UDP] {src_ip}:{src_port} -> {dst_ip}:{dst_port}"
        print(Fore.CYAN + message)
        log_packet(message)


def print_summary():
    print("\n--- Summary ---")
    print(f"Total packets: {packet_count}")
    print(f"TCP packets: {tcp_count}")
    print(f"UDP packets: {udp_count}")