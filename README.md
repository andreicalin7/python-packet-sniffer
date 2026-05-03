# Python Packet Sniffer

A Python-based network packet sniffer that captures, filters, and logs network traffic in real time.  
Supports protocol filtering (TCP/UDP), port filtering, timestamps, command-line configuration, and persistent logging.

---

## Features

- Capture live network packets using Scapy  
- Filter traffic by protocol (TCP / UDP)  
- Filter traffic by specific port (e.g. HTTPS 443)  
- Display source/destination IPs and ports  
- Add timestamps to all captured packets  
- Log captured packets to a file (`packets.log`)  
- Command-line configuration:
  - Protocol selection  
  - Packet count  
  - Timeout duration  
  - Port filtering  
- Summary statistics after execution  

---

## Tech Stack

- Python  
- Scapy  
- Colorama  
- Git  

---

## How It Works

The application listens for incoming and outgoing packets on your network interface.  
Each packet is analyzed to extract relevant information such as:

- Source IP  
- Destination IP  
- Source port  
- Destination port  
- Protocol type  

Filtered packets are:

1. Displayed in the terminal (color-coded)  
2. Logged to a file with timestamps for later inspection  

---

## Example Output

![Packet Sniffer Output](screenshot.png)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/andreicalin7/packet-sniffer.git
cd packet-sniffer
