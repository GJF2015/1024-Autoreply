from PIL import Image
import requests
import base64
import os
class Getver:
    def getcode(self):
        im=Image.open("image.webp")
        im.save('image.png')
        f=open('image.png','rb')
        image=base64.b64encode(f.read())
        url='http://302307.market.alicloudapi.com/ocr/captcha'

        Auth="APPCODE "+os.environ["TOKER"]
        headers={
            "Authorization":Auth,
            "gateway_channel":"http",
            "Host":"302307.market.alicloudapi.com",
            "Content-Type":"application/x-www-form-urlencoded;charset=utf-8"
        }
        data={
            'image':image,
            'length':'0',
            'type':'1001'
        }
        result=requests.post(url,headers=headers,data=data)
        res=result.text
        m=res.find('captcha')
        n=res.find('type')
        code=res[m+10:n-3]
        return code
