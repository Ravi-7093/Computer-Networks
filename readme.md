#UTA ID - 1002026832
#Name - Ravi Prakasha
1) Download the zip folder from the canvas.

2) Extract the folder.

3) Install visual studio code and requirements.txt file
    a) Steps to install visual studio code is given in 
        https://medium.com/nerd-for-tech/install-visual-studio-code-fe3908c5cf15
    b) Run the command pip3 install -r requirements.txt  to install all the required packages.

4) After installation click on File in visual studio code and click on Open Folder and select the extracted folder.

5) Click on Terminal and have two terminal opened on the same folder.

6) Then type the command python3 final_with_tst.py 5000 confir.config to run the first file in first terminal.

7) In the second Terminal run the command as python3 check_update.py 

8) Please input the data from the terminal for the first file i.e. in first terminal
   a) Enter the value for n the 'n' updates . Ex - 2
   b) Enter the ip_address to bind for the socket.  Ex - 127.0.0.1

9) Please input the data from the terminal for the second file i.e. in second terminal
   a)Enter the source ip_address in the network for which cost to be updated. Ex - 127.0.0.1
   b) Enter the destination ip_address in the network for which cost to be updated. Ex - 127.0.0.6
   c) Enter the cost to be updated . Ex - 2
   d) Enter the ip address to which you need to send data . Ex -127.0.0.1

10) The code runs until n updates and stops printing the final message.
