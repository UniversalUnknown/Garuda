from scapy.all import *
import os

# Function to handle packets
def packet_handler(packet):
    if packet.haslayer(Dot11):
        # Check if it's a probe request or beacon frame
        if packet.type == 0 and packet.subtype in [0, 4]:  # 0: Beacon, 4: Probe Request
            ssid = packet[Dot11Elt].info.decode() if packet[Dot11Elt].info else "Hidden SSID"
            bssid = packet[Dot11].addr2
            print(f"SSID: {ssid}, BSSID: {bssid}")

# Set the interface to monitor mode (Linux only)
def set_monitor_mode(interface):
    os.system(f"sudo airmon-ng start {interface}")

# Main function
def main(interface):
    set_monitor_mode(interface)
    print(f"Listening on {interface}...")
    sniff(iface=interface, prn=packet_handler, store=0)

if __name__ == "__main__":
    # Replace 'wlan0' with your Wi-Fi interface name
    main('lo')
