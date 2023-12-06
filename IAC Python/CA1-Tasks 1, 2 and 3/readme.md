### **CA1 Farmer Temperature Project*
This project is was designed to monitor a temperature from differente locations, the informations will be received from three UDP clients, a server will save the data in different logfiles and will allert the farmer when the temperatur is <5 celsious or >30 celsious degrees.

#### Script

The script is designed to read the udp inputs, check the temperature, trigger an alarme if is less than 5C or more than 30C, and finally save the logs in 3 different directories, one for each udp client.
