from pythonping import ping


def pinger(host):
    ping_result=ping(host, verbose=True,count=1)
    print(ping_result)
    f = open("result_[ping].txt", "a")
    f.write(str(ping_result))
    f.close()


host=input("please enter your ip/domain:")
pinger(host)
