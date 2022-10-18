from http.cookiejar import Cookie
import io
import ddddocr
import requests
from PIL import Image
import random
s=requests.session()
#编码pswd
#用户输入
id=input("用户账号>>>")
pswd=input("用户密码>>>")
def encode(pswd):
    staticchars = "hwPX71B0asDIAkUo5T9HKQzjCmGSYOx4yJ2FfZgL8vRNeVtpnE6cbrWlqMi3du"
    enstr= ""
    for char in pswd:
        num=staticchars.find(char)
        if num == -1 :
            code = char
        else:
            code = staticchars[(num+6)%62]

        num1= random.randint(0,61)
        num2= random.randint(0,61)
        enstr +=staticchars[num1]+code+staticchars[num2]
    return enstr
pswd=encode(pswd)

rr=s.get("http://sso.tidesec.com/index.php?m=seccode")
验证码 = rr.content
cok=rr.cookies["PHPSESSID"]
cook=rr.cookies.values()
for i in cook:
    nm=i
img = Image.open(io.BytesIO(验证码))
ocr = ddddocr.DdddOcr()
res = ocr.classification(img)
cookie={
    'PHPSESSID':nm,
}
data={
    'username' :id,
    'password' : pswd,
    'seccode': res,
}
r1=s.post(url='http://sso.tidesec.com/',data=data,cookies=cookie)
r2=s.get(url='http://sso.tidesec.com/index.php?m=index&a=nav')
print(r2.text)
print(rr.cookies.values())
print(s.cookies.values())
