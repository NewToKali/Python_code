Intended for Debian Linux. This is a network scanner that allows you to discover all devices in the subnet by sending an arp message with the broadcast mac address to all hosts in the subnet.

Prerequisites:

scapy.all
optparse
To install: 

pip install scapy.all 
pip install optparse

Usage:
--help  ---> will show available options
example: 
python Network_scanner.py -t <subnet like 10.0.0.1/24>

Note:
by default, this program will use the original NIC (eth0). If you intend to use this with an external NIC (wlan0) please turn off eth0.
