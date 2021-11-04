import scapy.all as scapy
import re
import csv
import utils.utils as ut
"""
Net Scanner class is a little bit better developped than Port scanner, cuz this one was supposed to be a class instead of portscanner
So, this class provides multiple methods to scan local network (ARP, DNS records, SOA, MX)
once an object has been instanciated, you can call the method one by one or directly perform a full scan

Note that single methods does not (yet) provide csv export, only the full scan permits it

"""

#TODO   add try catch where code could shit itself
#       add if statment to handle failed/no/empty resposes
#       add other scanning functionality such has AD detection and probing)
class net_scanner:

    def __init__(self, target_ip, qualified_name, verbose):
        self.ip = target_ip
        self.qdname = qualified_name
        self.verbose = scapy.conf.verb = verbose

    def arp_scan(self, ip, mask):
        print("-" * 37)
        print("\t\t\tBEGIN ARP SCAN")
        print("-" * 37)

        arp_results = {}
        arp_r = scapy.ARP(pdst=ip+"/"+str(mask))
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br/arp_r
        answered, unanswered = scapy.srp(request, timeout=1)
        print('\tIP\t\t\t\t\tMAC')
        print('_' * 37)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            arp_results[ip] = mac
            print(ip, '\t\t' + mac)
            print('-' * 37)

        return arp_results

    def dns_scan(self, dport, qname):
        print("-" * 37)
        print("\t\tBEGIN DNS A-TYPE RESOLV")
        print("-" * 37)
        ans = scapy.sr1(scapy.IP(dst=self.ip) / scapy.UDP(sport=scapy.RandShort(), dport=dport) / scapy.DNS(rd=1, qd=scapy.DNSQR(qname=qname, qtype="A")))
        print(ans.an.rdata)

    def soa_scan(self, dport, qname):
        print("-" * 37)
        print("\t\t\tBEGIN SOA SCAN")
        print("-" * 37)
        ans = scapy.sr1(scapy.IP(dst=self.ip) / scapy.UDP(sport=scapy.RandShort(), dport=dport) / scapy.DNS(rd=1, qd=scapy.DNSQR(qname=qname, qtype="SOA")))
        print("[INFO] Following Start of Authority has been found :"+str(ans.an.rname))
        return ans.an.rname

    def mx_scan(self, dport, qname):
        print("-" * 37)
        print("\t\t\tBEGIN MX SCAN")
        print("-" * 37)
        ans = scapy.sr1(scapy.IP(dst=self.ip) / scapy.UDP(sport=scapy.RandShort(), dport=dport) / scapy.DNS(rd=1, qd=scapy.DNSQR(qname=qname, qtype="MX")))
        results = [x.exchange for x in ans.an.iterpayloads()]
        print("[INFO] Following mail server has been found : "+str(results))
        return results

    def full_scan(self, dport, mask, qname):

        char_list = ["b", "'"]
        fields = ["IP", "MAC"]
        arp_results = {}
        soa_results = []
        mx_results = []

        arp_results = self.arp_scan(self.ip, mask)
        soa_results = self.soa_scan(dport, qname)
        mx_results = self.mx_scan(dport, qname)

        mod = ''.join(str(soa_results))
        soa_sanitized = re.sub('['+ ''.join(char_list)+']', '', mod)

        ut.export_csv_dict(arp_results, fields,"../dashboard/data/arp_result.csv")
        ut.export_csv_string(soa_sanitized, "../dashboard/data/soa_result.csv")
        ut.export_csv_list(mx_results, "../dashboard/data/mx_result.csv")

        print("[INFO] All results files have been exported to csv")