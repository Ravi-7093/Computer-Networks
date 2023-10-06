NAME :- RAVI PRAKASHA
STUDENT ID :- 1002026832



1) Download the folder from canavs  and unzip it

2) Open the terminal and Navigate the folder where it is downloaded 
   
   To open a terminal on a Mac:
     1)Click on the Launchpad icon (rocket ship) located in the Dock.
     2)Click on the "Utilities" folder, then click on "Terminal".

   To open a terminal on Windows:
    1)Click on the Start button located in the lower-left corner of the screen.
    2)In the search bar, type "Command Prompt" or "PowerShell".
    3)Click on the corresponding option that appears in the search results.

3) Install python 3.9 using the following link
    https://www.python.org/downloads/

4) After installing the python  execute the following commands in CMD or Terminal
   
    pip3 install sys
    pip3 install datetime
    pip3 install threading
    pip3 install socket
    pip3 install time
    

4) After installing the packages , Open CMD/Terminal and go to servy.py file within in the folder


    python3 servy.py <portNumber>
    Eg:- python3 servy.py 8080

    Default port number is 8080

5)Open another CMD/Terminal and go to clieny.py file within the folder


    python3 client.py <IPADDRESS> <portNumber> <FILENAME>
    Eg:- python3 server.py 127.0.0.1 8080 text.txt

    Default IPAddress Number is 127.0.0.1
    Default port number is 8080
    Default File is text.txt



6) To Run On Web Browser

    Once the server program is running open your browser and type the following url
    http://localhost:portnumber/filename

    Below is the example
    http://localhost:8080/text.txt 

