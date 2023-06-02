import socket
from datetime import datetime
from time import time_ns
size = 1024
address_port = ("35.231.27.109", 32123)

client_msg = 'TIME'
encoded_msg = str.encode(client_msg)
UDP_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

before = datetime.now()
UDP_client.sendto(encoded_msg, address_port)
recieved = UDP_client.recv(size).decode()
After = datetime.now()
rtt = before - After
new_time  = ((rtt/2) + before)
time_dff = datetime.fromisoformat(recieved) - new_time

print("Time Before:\t" + str(before))
print("Time Received:\t" + recieved)
print("Time After:\t" + str(After)+"\n")
print("RTT:\t0:00:00.0"  + str(rtt.seconds)+"\n")
print("Time Difference:\t-0.0"  + str(time_dff.seconds))




