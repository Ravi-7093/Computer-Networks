# NAME - RAVI PRAKASHA
# UTA ID -1002026832

import time
import sys
import socket #using socket module to make used of sockets for client and server communication

default_Serv_IPaddrss = "127.0.0.1" # using default IP address if IP address is not specified by the use
default_Port = 8080 #using default port number if port number not specified by the user
fname = "/text.txt" #the default text file used  if no text file is provided by the user 


class Check_Connection():#class to create connection 

    def __init__(self, default_serv_ipaddress, default_port, fname): #initalizing the values in the main class
        self.default_serv_ipaddress = default_serv_ipaddress #Initializing  the IP address
        self.default_port = default_port #Initializing the port number 
        self.fname = fname #Initializing the file name

    def check_serve_connection(self):
        cnt_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies the model of the socket , AF_INET specifies the module uses IPV4 protocol and SOCK_STREAM uses TCP connection
        try:
   
            cnt_skt.connect((self.default_serv_ipaddress, self.default_port)) #client makes a connection to the server using the socket 
            st_tme = time.time() # used to calculate the round trip time it return time in seconds
            request = f"GET {self.fname} HTTP/1.1\r\nHost: {self.default_serv_ipaddress}\r\n\r\n" #send a get request to server ie the filename

            cnt_skt.sendall(request.encode()) #encode the request 
            fc_cntnt = b"" #Initializing the avariable that holds file data to null 
            data = cnt_skt.recv(1024) #recieve the value from the server into client socket 
            fc_cntnt+=data
            
            fc_cntnt=fc_cntnt.decode('utf-8')#decoding the data
            end_tme = time.time() # used to calculate the round trip time it return time in seconds
            ds_rtt= end_tme -st_tme

    

            header = fc_cntnt.split()[0] #spliting the result variable ie file data  to get the header 
          
         
            status_code = int(fc_cntnt.split()[1]) #spliting the result variable ie file data  to get the status_code 

           
        # check the status of http 
            if status_code== 200: #The HTTP 200 OK  status  code indicates that the request was successful.
               stat_cod= "200 OK\n" #assiging the 200 Ok code to stats_cod variable
            elif status_code == 404: #The HTTP 404 NOT FOUND  code indicates the file is not available
               stat_cod="404 NOT FOUND\n" 
            
            print("<------------------File Downloaded Successfully-------------------------->\n")
            
            print("File Name requested = "f'{self.fname}\n')#print the file name 

            print("The file contents. \n")

            data=fc_cntnt.split('\n')[3:]#splitting the data and headers within file_data
            new_str=""
            new_str=data[0:] # perform cleaning for only required value
            print(new_str,"\n")#printing the file data
            
            print("HTTP_Version = ",header) #print the header
            
            print("Status_Code = ", stat_cod) #print the stat_cod
         
            print("Server Port = ",self.default_port) ##print the server port number
            print("Host name of the Server = ", self.default_serv_ipaddress) #print the server_address
            print("Socket_family = ", cnt_skt.family) #print the socket family 
            print("Socket_type = ", cnt_skt.type) # get the type of scoket 
            print("Protocol Used By Socket = ", cnt_skt.proto)#print the socket type 
            print("Timeout = ", cnt_skt.gettimeout()) #used to get the time value of the socket 
            print("Peer name Used By Socket = ", cnt_skt.getpeername())#get the peer name 
            
            print(f"The round trip time is {ds_rtt:.5f} seconds")#displaying the round trip time 

        except ConnectionRefusedError:
            print(
                f'Error: Connection refused. Check if the server is running on {self.default_serv_ipaddress}:{self.default_port}')#check for connection reset 
        except OSError as e:
            print(f'Error: {e.strerror}')
        finally:
            cnt_skt.close()

def main():



    if len(sys.argv) == 3: #check if the length of arguments provided in the command line is 3
        check_host_name = sys.argv[1] #initialize the host name 
        default_serv_ipaddress =check_host_name #initialize the ip address 
        port_number = int(sys.argv[2])  #taking the input from the command line for port number 
        port= port_number #initialize the port number 
        print("No file is provided. Default file is used.\n")
        feNam = "/text.txt" #initializing the file name  

    elif len(sys.argv) == 4: #check if the length of arguments provided in the command line is 3
        check_host_name = sys.argv[1] #check for host name 
        default_serv_ipaddress =check_host_name #check for ipaddress 
        port_number = int(sys.argv[2]) #check for port number and intialize it 
        port= port_number
        file_name = "/"+sys.argv[3] # get the file name from the user through command lien 
        feNam = file_name #intialize the file name

    elif len(sys.argv) == 2: #check if the length of arguments provided in the command line is 2
        check_host_name = sys.argv[1] #initialize the host name 
        default_serv_ipaddress =check_host_name #initialize the ip address 
        print("No port no is provided. Default value 8080 is used.\n")
        check_port = 8080 #initialize the port 
        print("No file is provided. Default file is used.\n")
        feNam="/text.txt"
    else:
        default_serv_ipaddress = "127.0.0.1" #if nothing provided then use the default values specified here  for IP address , port and file name 
        port = 8080
        feNam = "/text.txt"

    ck = Check_Connection(default_serv_ipaddress,port,feNam) #creating the object for the main class
    ck.check_serve_connection() #calling the check_serve_connection to make a request to the server 

if __name__ == '__main__':
    main()

