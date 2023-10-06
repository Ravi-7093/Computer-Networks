# NAME - RAVI PRAKASHA
# UTA ID -1002026832


import os
import socket #using socket module to make used of sockets for client and server communication
import sys 
import threading #using threading module to implement threading 

default_Serv_IPaddrss = "127.0.0.1" # using default IP address if IP address is not specified by the user
default_Port = 8080 #using default port number if port number not specified by the user
fname ='/text.txt' #the default text file used  if no text file is provided by the user 

class Check_Server(threading.Thread): #uses the thread class allowing it to run as seperate thread classes
    def __init__(self, cnt_skt, ck_address): #The self parameter refers to the instance of the object,name_host, number_port, name_file
        threading.Thread.__init__(self) #init method to intialiaze all the variables and properties
        self.cnt_skt = cnt_skt  #Initailizing the client socket 
        self.ck_address = ck_address #Initailizing the client address
        
    
   
    
    def check_file_exists(self,file): #function to check if file exists on the directory
        global fname #intializing a globe file variable 
        if file =="": #check if global variable is null 
            return fname
        else:
            if os.path.exists(file): #check if the file exists on the directory 
                #print(file,"in check file")
                return file #return the file 
            else :
                print("File not found on the directory") #print file not found on the directory 


    def run(self): #this method is used when thread starts 
        get_fname = self.cnt_skt.recv(1024).decode('utf-8') #it uses the client socket to get the data from client and the data being received is restricted to 1024 bytes at once
        print('Received file request for', get_fname, 'from', self.ck_address) #printing the address of the client from the request was received for the server 
        file_path=get_fname.split()[1][0:] #extracting only the filename from the get request
        chekfname = self.check_file_exists('.'+file_path)#call to check file function
        #print(chekfname,"filename")
        if chekfname:# if file is present
            try:
                with open(chekfname, 'rb') as file: #the file is opened from the binary mode to read the data
                    file_blb = file.read() #reading all the data into a file_blb varaible
                    response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(file_blb)}\r\n\r\n".encode() + file_blb #encoding the data and sending the resposne to client

                    self.cnt_skt.sendall(response)#sent the response to client
                    
                    print('Sent file contents to', self.ck_address)
            except FileNotFoundError: #exception handling to check if file is present or not
                    response = b"HTTP/1.1 404 Not Found\r\n\r\n" # error code sent to client 
                    self.cnt_skt.sendall(response) #response sent to client 
                    print(" 404 Not File Found response for ",self.ck_address)
        else:
            print("Error ")
        
        
    
   
def main(): #main function -->starts the program
    global default_Port #making variable global so that value can be accessed globally
    
    if len(sys.argv) <=1:
        default_Port = 8080 #default port is 8080 used
    else:
        default_Port = int(sys.argv[1])
    
    sev_skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #specifies the model of the socket , AF_INET specifies the module uses IPV4 protocol and SOCK_STREAM uses TCP connection
    sev_addr=(default_Serv_IPaddrss,default_Port) #used to specify the port and IP address of the socket for which the server will listen the incoming client requests
    sev_skt.bind(sev_addr)#binds the socket with server address
    sev_skt.listen(3) #specifies that the socket wil listen to maximum of 3 queued connections  
    print("Server started \n")
    while True :
        cnt_skt, ck_address = sev_skt.accept() #accept the incoming client connection over the socket
        client_thread = Check_Server(cnt_skt, ck_address)
        client_thread.start()#starts the thread and executes the run method on the thread created 

        print("Client Port Number =",ck_address[1]) #print the client port number
        print("Client Address =",ck_address[0])#print the client IP Address
        print("Socket_family = ", sev_skt.family) #print the socket family 
        print("Socket_type = ", sev_skt.type) #print the socket type 
        print("Protocol Used By Socket = ", sev_skt.proto) #print the protocol of the socket
        print("Timeout = ", sev_skt.gettimeout()) #used to get the time value of the socket 
    
if __name__ == '__main__':
    main()






