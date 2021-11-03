import scapy.all as scapy

"""
For testing purposes only

"""
from net_scanner import nscanner_class


scanner = nscanner_class.net_scanner("10.0.0.101", "best-energies.fr", 0)

#scanner.soa_scan(53, "best-energies.fr")

scanner.full_scan(53, 24, scanner.qdname)