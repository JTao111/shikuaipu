import hashlib
import requests
cmsdict={}
with open('cms.txt','r',encoding='utf8') as f :
    for line in f :
        l=line.strip().split('|')  # [url,cms,hash]
        t=(l[1],l[2])
        cmsdict.setdefault(l[0],[]).append(t)
def scancms(host):
    for url in cmsdict:
        httpurl='http://'+host+url
        try:
            r=requests.get(url=httpurl,timeout=2)
        except Exception as e :
            pass
        if r.status_code == 200 :
            hashcode=hashlib.md5(r.content).hexdigest()
            for hashcms in cmsdict[url]:
                if hashcms[1]==hashcode:
                    print('此cms:{}'.format(hashcms[0]))
                    return
        else:
            continue
    else:
        print("未找到对应cms")
scancms('www.wpchina.org') 