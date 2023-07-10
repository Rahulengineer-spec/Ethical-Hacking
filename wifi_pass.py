import subprocess

def get_wifi_password(ssid):
    try:
        # Run the netsh command to retrieve the Wi-Fi password for the specified SSID
        result = subprocess.run(['netsh', 'wlan', 'show', 'profile', 'name=' + ssid, 'key=clear'], capture_output=True, text=True)
        output = result.stdout

        # Search for the Key Content field in the output
        key_content_index = output.find("Key Content")
        if key_content_index != -1:
            # Extract the password after the colon
            password = output[key_content_index + 13:].splitlines()[0]
            return password
        else:
            return None

    except subprocess.CalledProcessError:
        return None

# Specify the SSID of the Wi-Fi network for which you want to retrieve the password
ssid = "shabad 2.4g"

# Retrieve the Wi-Fi password
password = get_wifi_password(ssid)
if password:
    print(f"The password for Wi-Fi network '{ssid}' is: {password}")
else:
    print(f"Unable to retrieve the password for Wi-Fi network '{ssid}'")
