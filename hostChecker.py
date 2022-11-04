import nmap

def host_scanner(host,starting_port,last_port):
 nm = nmap.PortScanner()
 #22-443
 args=["-sS","-sT","-sA","-sW","-sM",'-sN','-sF','-sX','-sU','-sY','-sZ','-sO','-b','-O']
 port_bitmap=dict()
 for i in range(starting_port,last_port + 1):
     port_bitmap[i]=-1
 for arg in args:
  nm.scan(host, str(starting_port)+"-"+str(last_port),arguments=arg)
  for host in nm.all_hosts():
   for proto in nm[host].all_protocols():
    for port in nm[host][proto].keys():
        port_bitmap[port]=1 if nm[host][proto][port]['state']=='open' else 0
 for key in port_bitmap.keys():
  status=None
  if port_bitmap[key]==1:status="open"
  elif port_bitmap[key]==0:status="close"
  else:status="filtered"
  print("port "+str(key)+" is "+status)



# host=input("Enter the ip to scan:")
host='127.0.0.1'
# starting_port=input("Enter the start port number:")
# last_port=input("Enter the last port number:")
starting_port=22
last_port=443
host_scanner(host,starting_port,last_port)