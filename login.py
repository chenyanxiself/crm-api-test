#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:57
# @Author  : yxChen
import time,os,json
from PIL import Image
from aip import AipOcr
from config import Config

class Login:
    def __init__(self,session,user):
        self.uuid=int(time.time())
        self.session=session
        self.relogin_count = 10
        self.user:dict=user
    def get_login_session(self):
        for i in range(self.relogin_count):
            verify_code=self.get_login_verify_code()
            data = self.user
            data.setdefault('verifyCode',verify_code)
            data.setdefault('uuid',self.uuid)
            res = self.session.post(Config.login_url, data=data)
            if res.status_code!=200:
                raise SyntaxError(f'登录接口返回码异常 :{res.status_code}')
            else:
                res_json:dict = json.loads(res.text)
                if res_json.get('code') == 0:
                    token = res_json.get('Admin-Token')
                    self.session.headers.setdefault('Admin-Token',token)
                    return self.session

    def get_login_verify_code(self):
        res = self.session.get(url=Config.verify_img_url,params={'uuid':self.uuid}).content
        init_path:str=os.path.dirname(os.path.realpath(__file__)) + '/image'+ f'/{self.uuid}.png'
        processed_path:str=os.path.dirname(os.path.realpath(__file__)) + '/image'+ f'/{self.uuid}_process.png'
        with open(init_path, 'wb') as f:
            f.write(res)
        #处理图片
        img = Image.open(init_path)
        _image = img.convert('L')
        pixels = _image.load()
        for x in range(_image.width):
            for y in range(_image.height):
                if pixels[x, y] > 127.5:
                    pixels[x, y] = 255
                else:
                    pixels[x, y] = 0
        _image.save(processed_path)
        with open(processed_path, 'rb') as fp:
            processed_img = fp.read()
            client = AipOcr(**Config.baidu_config)
            result = client.basicAccurate(processed_img)
            text = '\n'.join([w['words'] for w in result['words_result']]).replace(' ', '')
        os.remove(init_path)
        os.remove(processed_path)
        return text



if __name__ == '__main__':
    import requests
    from config import Config
    s=requests.Session()
    Login(s,Config.admin_user).get_login_session()