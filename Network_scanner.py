#!/usr/bin/env python
import scapy.all as scapy
import optparse
 
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="ip", help="choose the ip which u want to find")
    # return parser.parse_args()
    (options, arg) = parser.parse_args()
    if not options.ip:
        parser.error("please specify an interface type help for more info")
 
    return options
def scan(ip):
 
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    #answerd_list , unanswerd_lits = scapy.srp(arp_request_broadcast, timeout= 1)
    answerd_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False )[0]
    # print(answerd_list.summary())
    # print("IP\t\t\t\t MAC ADDRESS\n----------------------------------------------------")
    listOfScan = []
    for packet in answerd_list :
        # print(packet[1].show())
        dictionary = {"ip": packet[1].psrc, "mac": packet[1].hwsrc}
        # print(packet[1].psrc +"\t\t\t" +packet[1].hwsrc)
        listOfScan.append(dictionary)
 
    # print(listOfScan)
    return listOfScan
    # arp_request_broadcast.show()
    # print(arp_request.summary())
    # scapy.arping(ip)
    # scapy.ls(scapy.ARP())
def print_results(list_scan):
    print("IP\t\t\t\t MAC ADDRESS\n----------------------------------------------------")
    for client in list_scan:
        print(client["ip"]+"\t\t\t"+client["mac"])
 
gotip = get_arguments()
scan_resuts = scan(gotip.ip)
print_results(scan_resuts)

