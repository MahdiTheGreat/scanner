import nmap

def host_scanner(host,starting_port,last_port):
 nm = nmap.PortScanner()
 output=""
 output +="unspecified ports are closed\n"
 args=["-sS","-sT","-sA","-sW","-sM",'-sN','-sF','-sX','-sO','-sU -sY -sZ']
 port_status=dict()
 for arg in args:

  nm.scan(host, str(starting_port)+"-"+str(last_port),arguments=arg)
  for host in nm.all_hosts():
   for proto in nm[host].all_protocols():
    for port in nm[host][proto].keys():
     if (port in port_status.keys() and port_status[port]!='open') or port not in port_status.keys():
            port_status[port]=nm[host][proto][port]['state']
 for port in port_status.keys():
   output +="port "+str(port)+" is "+port_status[port]+"\n"
 f = open("result_[portScanner].txt", "w+")
 f.write(output)
 f.close()
 print(output)


host=input("Enter the ip to scan:")
starting_port=int(input("Enter the start port number:"))
last_port=int(input("Enter the last port number:"))
# host='127.0.0.1'
# starting_port=22
# last_port=443
host_scanner(host,starting_port,last_port)