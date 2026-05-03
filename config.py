import sys

FILTER_PROTOCOL = "TCP"
PACKET_COUNT = 20
TIMEOUT = None
PORT_FILTER = None

if len(sys.argv) > 1:
    FILTER_PROTOCOL = sys.argv[1].upper()

if len(sys.argv) > 2:
    PACKET_COUNT = int(sys.argv[2])

if len(sys.argv) > 3:
    TIMEOUT = int(sys.argv[3])

if len(sys.argv) > 4:
    PORT_FILTER = int(sys.argv[4])