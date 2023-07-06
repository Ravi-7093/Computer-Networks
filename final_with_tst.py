#UTA ID - 1002026832
#Name - Ravi Prakasha

import argparse
import socket
import json
import time 


#Receiving the arguments to run the file 
rp = argparse.ArgumentParser(description='UDP Router') # Initial description for the command line argument to take from the user  
rp.add_argument('port', type=int, help='the port number to listen on')# command line input for port from the user 
rp.add_argument('cf_fle', type=str, help='the path to the configuration file')# command line input for config_file from the user 
args = rp.parse_args()
port = args.port# get the port from the argument provided by the user 
new_cnt = 0  # Initialize update counter
ps_sze = 0  # Initialize payload size

def BellmanFord(config, source):
    my_pew = [] #create an empty list 
    for a, b, c in config: #iterate the config table 
        my_pew.append((a, b, int(c)))  #append the source ,destination of the router along with the cost
        my_pew.append((b, a, int(c)))
    dst = {}
    for node in nodes: #initialize the distance for very high value except for source node provided as input to Bellman Ford
        dst[node] = infi
    dst[source] = 0
    
    for i in range(1, len(my_pew)):
        for a, b, c in my_pew: #check if the path cost can be improved for each destination router from source router 
            if dst[a] + c < dst[b]:
                dst[b] = dst[a] + c
    
    for a, b, c in my_pew:
        if dst[a] + c < dst[b]:
            return "Negative cycle detected" #check for negative cycles
    
    return dst


# Initialize the values required to run the main code
infi = float('inf')
st_gsm="" #message printing variable for Test Case 1
num = int(input("Enter the number for the 'n' updates\n")) # get input from user from command line for n updates according to test 1

confi = [] #create a list 
with open(args.cf_fle, 'r') as fle: #open the config file 
    for li in fle: #read the config fig file line by line 
        rv_line = li.strip() #strip to remvove any spaces
        if rv_line:
            confi.append(tuple(rv_line.split())) #split the values in each line to get source , destination and cost according to space


config = [list(t) for t in confi] #make it as list 
print('<------------>Network  Topology:<------------->')

for i in config:
    print(f'{i[0]} ------> {i[1]} ------> {i[2]}') #print the toplogy of the network

skts = {} #socket dictionary
for i in config: #read the config table 
    if i[0] not in skts:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#Initializing the socket 
        skts[i[0]] = sock #socket for each router 
        print(f'Created socket for router {i[0]}') #create socket for each router 
        skts[i[0]].connect((i[1], args.port)) #connect ip address of each router to socket 
        print(f'Socket for router '+ i[0]+ ' bound to port '+ str(port)+'\n')

my_ra_rtrs = set() # create a set of routers from the config 
for i in config:
    my_ra_rtrs.add(i[0])
    my_ra_rtrs.add(i[1])
nodes=sorted(my_ra_rtrs) #sort the set 


bl_lst=[]

for n in nodes:# iterate through each router 
    kst = BellmanFord(config, n)# call the bellman ford algorithm intially to calculate least path from source 
    print(f'<-------->Shortest Distance from {n} to:<------------->')
    for i, j in kst.items():
        bl_lst.append([n,i,j])
        print(f'{i} -> {j}')
 

ip_address = input("Enter the ip_address to bind\n") #Enter the ip address to bind to the socker
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip_address, port))#binding ip  address  to socket
print(f"Router  Listening on port 5000")




while True:
    for node in nodes:
        #print(node,'---->node')
        # Listen for updates
        dt, addr = sock.recvfrom(1024)#module to get bytes of data from the 
        rsv_mxg = dt.decode('utf-8')#data encoded using UTF-8
        print(f'Received message from {addr}: {rsv_mxg}')
        print('')
        new_cnt = new_cnt + 1
        ps_sze += len(rsv_mxg.encode('utf-8')) #get payload size
        # Parse the received message
        msg = json.loads(rsv_mxg) #convert to json
        recv_srce = msg['source'] #get the source from the neighbour
        recv_dst = msg['destination']#get the source from the destination
        recv_cst = msg['cost']#get the source from the cost
        #print(recv_cost)
        
        #Update the routing table if necessary
        udt = False
        for i in range(len(bl_lst)):#iterate over the config 
            source, dest, cost = bl_lst[i]
            old_cost=cost
            if (source == recv_srce and dest == recv_dst):#check if source exists and destination
                if recv_cst < int(cost) :  #check if received cost is less than current cost 
                    print("I am updating the cost")
                    print('')
                    bl_lst[i][2] = recv_cst #if true update the cost 
                    udt = True
                    print(f'Update for router {recv_dst}:\n'
                          f'Source IP (Host): {recv_srce}\n'
                          f'Current Cost (updated value): {recv_cst}\n'
                          f'Previous Cost: {old_cost}\n')

        if udt:# if true 
            for node in nodes:
                p = BellmanFord(bl_lst, node) # call BellmanFord again since the cost updated 
                print(f'-------->Shortest Distance from {node}:<-------------')
                for k, v in p.items():
                    print(f'{k} -> {v}')
        if new_cnt == int(num):  # Change the value to the desired number of updates
           
            date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())  #To  get the current date and time in UTC
            
            st_gsm = f'Message from Router {node}, IP address {ip_address}, Port No. {port}. \n'# creating the final message with timestamps , UTA ids
            st_gsm += f'Date and Timestamp in UTC: {date_time}. \n'
            st_gsm += f'UTA-ID = 1002026832 , 1002078961. \n'
            st_gsm += f'Total number of updates: {num}. \n'
            st_gsm += f'Payload size for last broadcast: {ps_sze} bytes.'

            print(st_gsm)

            for nei in skts:
                skts[nei].send(st_gsm.encode('utf-8'))#  send updates to all sockets  
            
            for nei in skts:
                skts[nei].close()#close all the sockets of all the routes 
                sock.close()
            print('')              
            time.sleep(10)#time to sleep
            exit(0)  
    