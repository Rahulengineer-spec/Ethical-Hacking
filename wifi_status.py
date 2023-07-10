import requests

def get_connected_devices():
    # Perform network scanning or retrieve the list of connected devices from your network infrastructure

    # For demonstration purposes, let's assume we have a predefined list of devices
    connected_devices = ['192.168.1.10', '192.168.1.20', '192.168.1.30']
    
    return connected_devices

def send_welcome_message(ip_address, message):
    # Send an HTTP request with the welcome message to the target device
    url = f'http://{ip_address}/welcome'
    payload = {'message': message}
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(f"Welcome message sent to {ip_address}")
        else:
            print(f"Failed to send welcome message to {ip_address}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the welcome message to {ip_address}: {str(e)}")

# Configuration
wifi_ip_address = '192.168.1.33'  # Replace with your WiFi router's IP address
message = "Welcome to my network!"

# Get the list of connected devices
connected_devices = get_connected_devices()

# Send the welcome message to each connected device
for device in connected_devices:
    send_welcome_message(device, message)
