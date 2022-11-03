from pythonping import ping
import ipaddress
from time import time

def ip_range_scanner(host,starting_number,last_number):
    print("scanning in progress \n")
    begin_time=time()
    host = host.split('.')
    start_ip=ipaddress.IPv4Address(".".join(host[0:len(host)-1]+[str(starting_number)]))
    end_ip=ipaddress.IPv4Address(".".join(host[0:len(host)-1]+[str(last_number)]))
    for ip_int in range(int(start_ip), int(end_ip)):
        ip=str(ipaddress.IPv4Address(ip_int))
        print()
        ping_result = ping(ip, verbose=True, count=1)
        if ping_result.packet_loss != 1:
            print(str(ip)+"--->live")
    print("scanning complete in "+str((time() - begin_time))+" seconds")


host=input("Enter the network address:")
starting_number=input("Enter the starting number:")
last_number=input("Enter the last number:")
ip_range_scanner(host,starting_number,last_number)
