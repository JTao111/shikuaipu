from IPy import IP
import socket
from concurrent.futures import ThreadPoolExecutor
iplist=IP('172.16.124.213')  #ip段
def shuai(ip,port):
    s=socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
    ipport=(str(ip),port)
    print(ipport)
    s.settimeout(2)
    exp=s.connect_ex(ipport)
    if  exp :
        # print(ip+':'+str(port)+'   is closed') 
        pass
    else:
        print(ip+':'+str(port)+'   is open') 
if __name__ == '__main__':
    with ThreadPoolExecutor(100) as t:  #线程池数量
        for p in iplist:
            for i in range(21,25):  #端口段
                t.submit(shuai,str(p),i)
    print("all is ok")