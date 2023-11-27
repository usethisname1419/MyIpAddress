#!/usr/bin/env python3

import socket
import psutil
import argparse

def get_public_ip():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    public_ip = s.getsockname()[0]
    s.close()
    return public_ip

def get_network_info():

    network_info = {}
    for interface, addrs in psutil.net_if_addrs().items():
        interface_info = []
        for addr in addrs:
            if addr.family == socket.AF_INET:
                interface_info.append({
                    "ip": addr.address,
                    "netmask": addr.netmask,
                    "broadcast": addr.broadcast
                })
            elif addr.family == psutil.AF_LINK:
                interface_info.append({
                    "mac": addr.address,
                    "type": addr.family
                })
        network_info[interface] = interface_info
    return network_info

def get_open_ports():

    open_ports = []
    for conn in psutil.net_connections(kind='inet'):
        port = conn.laddr.port
        try:
            service_name = socket.getservbyport(port)
        except (OSError, socket.error):
            service_name = "Unknown"
        open_ports.append({"port": port, "service": service_name})
    return open_ports

def main():
    parser = argparse.ArgumentParser(description='Get public IP, local network interface info, and open ports.')
    parser.add_argument('-p', '--ports', action='store_true', help='List all open ports with service names')
    args = parser.parse_args()

    public_ip = get_public_ip()
    print(f"Public IP Address: ")
    print(f"  IP Address: {public_ip}")
    network_info = get_network_info()
    print("\nLocal Network Interface Information:")
    for interface, info in network_info.items():
        print(f"\nInterface: {interface}")
        for entry in info:
            if "ip" in entry:
                print(f"  IP Address: {entry['ip']}")
                print(f"  Netmask: {entry['netmask']}")
                print(f"  Broadcast: {entry['broadcast']}")
            elif "mac" in entry:
                print(f"  MAC Address: {entry['mac']}")
                print(f"  Type: {entry['type']}")

    if args.ports:
        open_ports = get_open_ports()
        print("\nOpen Ports:")
        for port_info in open_ports:
            print(f"  Port: {str(port_info['port']).ljust(5)} Service: {port_info['service']}")

if __name__ == "__main__":
    main()
