import requests
import hashlib
import queue
import threading
q=queue.Queue()
url1=input("请输入网站>>>")
cmsdict={}
with open('D:\\vmpython\\venv\\cms.txt','r',encoding='utf-8') as f:
    for line in f:
        q.put(line.strip().split("|"))
        # print(m)
        # break
def shuai(q,url1):
    while not q.empty():
        n=q.get()
        header={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
        }       
        try:
            r=requests.get(url='http://'+url1+n[0],headers=header,timeout=2) 
        except Exception as e:
            pass
        if r.status_code == 200:
            conhash=hashlib.md5(r.content).hexdigest()
            if conhash==n[2]:
                print("{}，采用{}CMS".format(url1,n[1]))
                return
            else:
                continue
    print('no cms')
list=[]    
for i in range(10):
    t = threading.Thread(target=shuai,args=(q,url1))
    t.start()
    list.append(t) 
for t in list:
    t.join()

# shuai('www.niehuihua.com')
