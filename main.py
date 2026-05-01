from colorama import init, Fore
from scapy.all import sniff

from config import FILTER_PROTOCOL
from sniffer import packet_callback, print_summary


init(autoreset=True)

print(Fore.YELLOW + f"Starting packet sniffer with filter: {FILTER_PROTOCOL}")

sniff(prn=packet_callback, count=20)

print_summary()