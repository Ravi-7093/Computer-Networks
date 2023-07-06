#UTA ID - 1002026832
#Name - Ravi Prakasha
import json
import socket
import time


src= input("Enter the source ip_address\n") #give the input for the source from where the cost has to be updated
des= input("Enter the destination ip_address\n")#give the input for the destination from where the cost has to be updated
cost = input("Enter the cost to be update\n")#give the cost update value
cs = int(cost)
upd = {
    "source": src,
    "destination": des,
    "cost": cs
} #create a message to send updatet to main network

# Create the neighbor router's IP address and port number
gh_ip = input("Enter the ip address to which you need to send data\n")
gh = 5000

# Creation of  UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# iteratively send mesage every 15 seconds
while True:
    # Send the update message to the neighbor router
    print("Sending update message:", upd)
    sock.sendto(json.dumps(upd).encode(), (gh_ip, gh))
    time.sleep(15)
