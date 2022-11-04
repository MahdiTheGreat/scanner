from pythonping import ping
import socket


def pinger(host):
    size=4
    ping_result=ping(host, verbose=False,count=1,size=size)
    ipaddress=socket.gethostbyname('www.google.com')
    output="paging "+host+"["+ipaddress+"] with "+str(28+size)+" bytes of data:\n\n"
    output+=str(ping_result)+"\n"
    ping_result=vars(ping_result)
    packets_lost=ping_result['stats_packets_sent']-ping_result['stats_packets_returned']
    loss_ratio=packets_lost/ping_result['stats_packets_sent']
    output +='packets sent: '+str(ping_result['stats_packets_sent'])+'\n'
    output += 'packets returned: ' + str(ping_result['stats_packets_returned']) + '\n'
    output += 'packets lost: ' + str(packets_lost) + '\n'
    output += 'lost ratio: ' + str(loss_ratio) + '\n'
    f = open("result_[ping].txt", "w+")
    print(output)
    f.write(output)
    f.close()


host=input("please enter your ip/domain:\n")
pinger(host)
