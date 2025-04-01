#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Network Interface Monitor
A tool for monitoring network interfaces lo and wlo1.
"""

import subprocess
import time
from dataclasses import dataclass
from typing import List, Dict, Optional
import json
import argparse

class Colors:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    CYAN = '\033[36m'

@dataclass
class InterfaceStats:
    """Statistics for a network interface"""
    name: str
    state: str
    rx_bytes: int
    tx_bytes: int
    rx_packets: int
    tx_packets: int
    mtu: int

class NetworkMonitor:
    """Monitors network interfaces"""
    def __init__(self, interfaces: List[str]):
        self.interfaces = interfaces
        self._validate_interfaces()

    def _validate_interfaces(self) -> None:
        """Verify that specified interfaces exist"""
        for interface in self.interfaces:
            if not self._interface_exists(interface):
                raise ValueError(f"Interface {interface} does not exist")

    def _interface_exists(self, interface: str) -> bool:
        """Check if an interface exists"""
        try:
            subprocess.run(
                ["ip", "link", "show", interface],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True
            )
            return True
        except subprocess.CalledProcessError:
            return False

    def get_interface_stats(self, interface: str) -> Optional[InterfaceStats]:
        """Get statistics for a specific interface"""
        try:
            # Get interface state
            state_output = subprocess.check_output(
                ["ip", "link", "show", interface],
                text=True
            )
            state = "UP" if "UP" in state_output else "DOWN"

            # Get interface statistics
            stats_file = f"/sys/class/net/{interface}/statistics"
            with open(f"{stats_file}/rx_bytes") as f:
                rx_bytes = int(f.read())
            with open(f"{stats_file}/tx_bytes") as f:
                tx_bytes = int(f.read())
            with open(f"{stats_file}/rx_packets") as f:
                rx_packets = int(f.read())
            with open(f"{stats_file}/tx_packets") as f:
                tx_packets = int(f.read())
            
            # Get MTU
            with open(f"/sys/class/net/{interface}/mtu") as f:
                mtu = int(f.read())

            return InterfaceStats(
                name=interface,
                state=state,
                rx_bytes=rx_bytes,
                tx_bytes=tx_bytes,
                rx_packets=rx_packets,
                tx_packets=tx_packets,
                mtu=mtu
            )
        except (subprocess.CalledProcessError, FileNotFoundError, ValueError) as e:
            print(f"{Colors.RED}Error getting stats for {interface}: {str(e)}{Colors.RESET}")
            return None

    def monitor(self, interval: int = 1) -> None:
        """Monitor interfaces and display statistics"""
        previous_stats: Dict[str, InterfaceStats] = {}
        
        try:
            while True:
                print("\033[2J\033[H")  # Clear screen and move cursor to top
                print(f"{Colors.CYAN}Network Interface Monitor{Colors.RESET}")
                print("-" * 80)
                
                for interface in self.interfaces:
                    stats = self.get_interface_stats(interface)
                    if not stats:
                        continue

                    # Calculate speed if we have previous stats
                    if interface in previous_stats:
                        prev_stats = previous_stats[interface]
                        rx_speed = (stats.rx_bytes - prev_stats.rx_bytes) / interval
                        tx_speed = (stats.tx_bytes - prev_stats.tx_bytes) / interval
                    else:
                        rx_speed = 0
                        tx_speed = 0

                    # Update previous stats
                    previous_stats[interface] = stats

                    # Display interface information
                    state_color = Colors.GREEN if stats.state == "UP" else Colors.RED
                    print(f"\nInterface: {Colors.BLUE}{interface}{Colors.RESET}")
                    print(f"State: {state_color}{stats.state}{Colors.RESET}")
                    print(f"MTU: {stats.mtu}")
                    print(f"RX: {self._format_bytes(stats.rx_bytes)} "
                          f"({self._format_speed(rx_speed)}/s)")
                    print(f"TX: {self._format_bytes(stats.tx_bytes)} "
                          f"({self._format_speed(tx_speed)}/s)")
                    print(f"Packets RX/TX: {stats.rx_packets}/{stats.tx_packets}")

                time.sleep(interval)

        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Monitoring stopped by user{Colors.RESET}")

    def _format_bytes(self, bytes: int) -> str:
        """Format bytes into human readable format"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if bytes < 1024:
                return f"{bytes:.2f} {unit}"
            bytes /= 1024
        return f"{bytes:.2f} TB"

    def _format_speed(self, bytes_per_sec: float) -> str:
        """Format speed into human readable format"""
        return self._format_bytes(bytes_per_sec)

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="Network Interface Monitor")
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=1,
        help="Update interval in seconds (default: 1)"
    )
    args = parser.parse_args()

    try:
        monitor = NetworkMonitor(['lo', 'wlo1'])
        monitor.monitor(interval=args.interval)
    except Exception as e:
        print(f"{Colors.RED}Error: {str(e)}{Colors.RESET}")
        return 1
    return 0

if __name__ == "__main__":
    exit(main())
