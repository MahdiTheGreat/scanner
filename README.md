# scanner
The output of the each code will be stored in a file named result_[ActionName].txt. 
For example, the Python code file related to the ping part of the project should be named ping.py and its output should be in the format result_ping.txt.
In the host scanner we scan a host to find it's open ports via the help of nmap library.
In the ip scanner we 
Getting a ping from a specific IP
• Scan an IP range and find active hosts
• Scan the open ports of an active host
The ping part should work with both IP and domain name and its output is as follows:
The output of scanning the IP range and finding active hosts:
Output of open ports scan of active hosts:

#Ping implementation

To implement ping, we use the pythonping library, whose translation for the google.com domain can be seen below:

![image](https://github.com/MahdiTheGreat/scanner/assets/47212121/d371d3f4-79af-4d3d-bc56-8d419eabbfa7)

#Implementation of IP range scanner

To implement it, we use the nmap library. First we use all kinds of probe packages to get a response from the active hosts, and if we don't receive responses from the hosts, we use the Pn mode to see if the famous service ports such as http and... on
these hosts are open or closed, and if they are open, we assume the related service is active.
It's getting late:
