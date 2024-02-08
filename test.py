import nmap
nm = nmap.PortScanner()
nm.scan('127.0.0.1', "500-1000",arguments="-sS")
print()
status=False
for host in nm.all_hosts():
 for proto in nm[host].all_protocols():
  for port in nm[host][proto].keys():
      if nm[host][proto][port]['state']=='open':status=True
print()