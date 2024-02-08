from pythonping import ping
import ipaddress
from time import time
import nmap

def ip_range_scanner(base_host,starting_number,last_number):
    output=""
    begin_time=time()
    up_hosts = set()
    nm = nmap.PortScanner()
    base_host = base_host.split('.')
    starting_host=str(ipaddress.IPv4Address(".".join(base_host[0:len(base_host) - 1] + [str(starting_number)])))
    end_host = str(ipaddress.IPv4Address(".".join(base_host[0:len(base_host) - 1] + [str(last_number)])))
    host =  starting_host+"-"+str(last_number)
    nm.scan(host, arguments='-sn -PS -PA -PU -PY -PE -PP -PM -PO')
    up_hosts=up_hosts|set(nm.all_hosts())
    temp={str(ipaddress.IPv4Address(ip_int)) for ip_int in range(int(ipaddress.IPv4Address(starting_host)), int(ipaddress.IPv4Address(end_host)))}
    filtered_hosts=temp - up_hosts
    print()
    for ip in filtered_hosts:
        nm.scan(ip, arguments='-Pn')
        status = False
        for host in nm.all_hosts():
            for proto in nm[host].all_protocols():
                for port in nm[host][proto].keys():
                    if nm[host][proto][port]['state'] == 'open':
                        status=True
                        break
        if status:up_hosts = up_hosts | set(nm.all_hosts())
    sorted_up_hosts = sorted(list(up_hosts))
    for host in sorted_up_hosts:
        output+=host + "--->live\n"
    output += "scanning complete in "+str((time() - begin_time))+" seconds\n"
    f = open("result_[ipScanner].txt", "w+")
    f.write(output)
    f.close()
    print(output)


base_host=input("Enter the network address:")
starting_number=input("Enter the starting number:")
last_number=input("Enter the last number:")
# base_host='89.43.3.0'
# starting_number=60
# last_number=70
ip_range_scanner(base_host,starting_number,last_number)
