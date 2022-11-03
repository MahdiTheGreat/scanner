
import socket
def ip_range_scanner(ip,port_range):
    # print("went inside ipscanner")
    openPortsList = []
    for i in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect_ex((ip, i))
        if (conn == 0):
            openPortsList.append(i)
        s.close()
    print("list of open ports are")
    print(openPortsList)