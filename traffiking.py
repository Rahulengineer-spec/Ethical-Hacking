import os
import socket
import pyshark

def get_wifi_interface():
    interfaces = os.listdir('/sys/class/net/')
    for interface in interfaces:
        if "Wi-Fi" in interface:
            return interface
    return None

def process_packet(pkt):
    if "http" in pkt:
        ip_src = pkt.ip.src
        ip_dst = pkt.ip.dst
        method = pkt.http.request_method
        host = pkt.http.host
        path = pkt.http.request_uri

        # Save the captured information to a file
        with open("visited_sites.txt", "a") as file:
            file.write(f"Source IP: {ip_src}\n")
            file.write(f"Destination IP: {ip_dst}\n")
            file.write(f"Method: {method}\n")
            file.write(f"Host: {host}\n")
            file.write(f"Path: {path}\n")
            file.write("---------------------\n")

# Get the Wi-Fi interface name
wifi_interface = get_wifi_interface()
if wifi_interface is None:
    print("Wi-Fi interface not found. Please check your network configuration.")
else:
    # Start capturing packets on the Wi-Fi interface
    capture = pyshark.LiveCapture(interface=wifi_interface, bpf_filter="tcp port 80")
    capture.sniff(packet_count=0, timeout=None, prn=process_packet)
