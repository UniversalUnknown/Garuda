import subprocess

def list_wifi_connections():
    # List available Wi-Fi networks
    print("Available Wi-Fi networks:")
    result = subprocess.run(['nmcli', 'dev', 'wifi'], capture_output=True, text=True)
    print(result.stdout)

def connect_to_wifi(ssid, password):
    # Connect to a Wi-Fi network
    print(f"Connecting to {ssid}...")
    command = f'nmcli dev wifi connect "{ssid}" password "{password}"'
    subprocess.run(command, shell=True)
    print(f"Connected to {ssid}.")

if __name__ == "__main__":
    list_wifi_connections()
    
    # Replace 'Your_SSID' and 'Your_Password' with your Wi-Fi credentials
    ssid = "Your_SSID"
    password = "Your_Password"
    
    connect_to_wifi(ssid, password)