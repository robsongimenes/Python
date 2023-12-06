# Import socket module, that allow servers to communicate across the network
import socket
# Import the settings.udp saved in settings folder
import settings.udp as settings

# Import the os module, that allow us to interact with the operating system
import os

# csv to
import csv

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

LOGGING_DIR = "logs"

# Temperature threshold low/high in degrees Celsius
temperature_threshold_low = 5
temperature_threshold_high = 30

print(f"This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and begin listening")
print(f"Make sure the actual server IP address matches {UDP_IP} in the settings file")
print(f"This script has no error handling, by design")

# Create a dictionary to store the temperature of each client, parsing the date received and give an error if the data received is invalid
client_temperatures = {}

def parse_data(data):
    decoded_data = csv.reader([data.decode('utf-8')], delimiter=',')

    # Parse the data into an array to be returned
    for row in decoded_data:
        hostname = row[0]
        temperature = int(row[1])
        time = row[2]

    data_array = [hostname, temperature, time]

    # data_array has three values, 0-2
    return data_array

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((UDP_IP, UDP_PORT))
    print('Listening on', UDP_IP)

    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)

        parsed_data = parse_data(data)

        hostname = parsed_data[0]
        temperature = parsed_data[1]
        time = parsed_data[2]

        print(f"Hostname: {parsed_data[0]}, Temperature: {parsed_data[1]}, Time: {parsed_data[2]}")

       # if any (temperature < temperature_threshold_low or temperature > temperature_threshold_high for temperature in client_temperatures.values()):
        if (temperature < temperature_threshold_low or temperature > temperature_threshold_high):
            print(f"ALERT: {hostname} has a temperature of {temperature} degrees Celsius at {time}, triggering something...")

        # Create the directory path using the variable
        directory_path = f"{LOGGING_DIR}/{hostname}"

        # Check if the directory exists
        if not os.path.exists(directory_path):
            # If not, create the directory
            os.makedirs(directory_path)

        # Create or open the file within the directory in append mode
        # we use csv format to make it easier to read/process the data later
        with open(f"{directory_path}/log", "a") as file:
            file.write(f"{temperature},{time}\n")
