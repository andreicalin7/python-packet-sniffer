import sys

if len(sys.argv) > 1:
    FILTER_PROTOCOL = sys.argv[1].upper()
else:
    FILTER_PROTOCOL = "TCP"