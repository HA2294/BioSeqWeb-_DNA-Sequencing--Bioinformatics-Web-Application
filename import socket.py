import socket
size = 1024
address_port = ("35.231.27.109", 23185)

client_msg = "halazar2019"
encoded_msg = str.encode(client_msg)

UDP_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_client.sendto(encoded_msg, address_port)
msgFromServer = UDP_client.recv(size).decode()

print(msgFromServer)