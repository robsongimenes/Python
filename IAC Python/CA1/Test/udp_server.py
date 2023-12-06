# Import socket module, that allow servers to communicate across the network
import socket
# Import the settings.udp saved in settings folder
import settings.udp as settings

# csv to 
import csv

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]
BUFFER_SIZE = 1024

# Temperature threshold low/high
temperature_threshold_low = 5
temperature_threshold_high = 30

print(f'This is the UDP server, it will open a port at {UDP_IP}:{UDP_PORT} and begin listening')
print(f'Make sure the actual server IP address matches {UDP_IP} in the settings file')
print('This script has no error handling, by design')

# Create a dictionary to store the temperature of each client, parsing the date received and give an error if the data received is invalid
client_temperatures = {}

def parse_data(data):
    print(data)
    t = data.decode()
    
    y = csv.reader([data], delimiter=',')
    print(data)
    for row in y:
        hostname = row[0]
        temperature = int(row[1])
        time = row[2]

    print(hostname)
    print(temperature)
    print(time)

    data_array = [hostname, temperature, time]

    print(data_array)

    # y being the array, three values, 0-2
    return data_array

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind((UDP_IP, UDP_PORT))
    print('Listening on', UDP_IP)
    
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)

        parsed_data = parse_data(data)

        print(parsed_data)

        print(f"Hostname: {parsed_data[0]}, Temperate: {parsed_data[1]}, Time: {parsed_data[2]}")

        if parsed_data:
            client_id, temperature = parsed_data
            client_temperatures[client_id] = float(temperature)

        # Check if any client temperature exceeds the threshold
       # if any (temperature < temperature_threshold_low or temperature > temperature_threshold_high for temperature in client_temperatures.values()):
        if (temperature < temperature_threshold_low or temperature > temperature_threshold_high):
            print("Temperature alarm triggered!")
            # Perform actions when the alarm is triggered (e.g., send a notification)

        # Print the info needed
        #print(addr, data)
        # if hostname-dir exists
        #   touch file
        #     echo hostname, temp, time >> file


