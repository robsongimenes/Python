'''
UDPClient by: JOR
Send UDP packets to a particular address and port.
Alpha: 13FEB22
'''

import socket
import time
from datetime import datetime
import settings.udp as settings

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

HOSTNAME = "HOST_1"

# Temperature in degrees Celsius
# We use a constant value for now
TEMPERATURE = 20

print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

        # format the date and time for logging purposes
        # we use iso-8601 format to make it easier to sort the logs by date
        TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # format the message to be sent to the server
        # the format is: "HOSTNAME,TEMPERATURE,TIME"
        message = "{},{},{}".format(HOSTNAME, TEMPERATURE ,TIME)
        message = message.encode('utf-8')

        # actually send the message to the server
        s.sendto(message, (UDP_IP, UDP_PORT))

        # we need to decode the message to print it as it's bytes by default
        print(message.decode('utf-8'))
        time.sleep(10)
