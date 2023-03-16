import os
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("hostname is : " + hostname)
print("IP address is : " + IPAddr)