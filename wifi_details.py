import subprocess
import re

def get_available_networks():
    try:
        # Run the netsh command to get the list of available Wi-Fi networks
        result = subprocess.run(['netsh', 'wlan', 'show', 'networks'], capture_output=True, text=True)
        output = result.stdout

        # Use regular expressions to extract the SSID names from the output
        ssid_pattern = re.compile(r'SSID\s+\d+\s+:\s(.+)')
        ssids = ssid_pattern.findall(output)

        return ssids

    except subprocess.CalledProcessError:
        return []

# Get the list of available Wi-Fi networks
available_networks = get_available_networks()

# Print the list of available network SSIDs
print("Available Wi-Fi Networks:")
for ssid in available_networks:
    print(ssid)
