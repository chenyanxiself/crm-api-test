#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:24
# @Author  : yxChen

from login import Login
import requests,json,copy
from config import Config
from auth_const import list_test

class Main:
    def __init__(self):
        # session_admin = requests.Session()
        # self.session_admin: requests.Session = Login(session_admin, Config.admin_user).get_login_session()
        # session_tester = requests.Session()
        # self.session_tester: requests.Session = Login(session_tester, Config.test_user).get_login_session()

        s = requests.Session()
        s.headers.setdefault('Admin-Token', 'd6a54dd39f334172b351b98b502cb6d2')
        self.session_admin: requests.Session=s
        t = requests.Session()
        t.headers.setdefault('Admin-Token', 'cbe8f393c9b7434fa658c4c6f3643bfd')
        self.session_tester: requests.Session=t
    def start(self):
        self.domain(list_test,["3", "4", "5", "701", "2"])

    def domain(self,item,auth_list:list):
        for i in item:
            if i.get('children',None):
                auth_list.append(i['id'])
                self.domain(i['children'],auth_list)
            else:
                auth_res = self.session_admin.get(url=Config.base_host+'/social-api/sys/permission/queryRolePermissions',
                                 params={'_t': 1593591992, 'roleId': Config.test_user['role_id']})
                lastPermissionIds = []
                if auth_res.status_code!=200:
                    raise SystemError('获取权限列表失败')
                for j in json.loads(auth_res.text)['result']:
                    if j['selected'] == True:
                        lastPermissionIds.append(i['id'])
                data = {"roleId":Config.test_user['role_id'],"permissionIds":auth_list,"lastPermissionIds":lastPermissionIds,"objectPermissions":[]}
                admin_res = self.session_admin.post(url=Config.base_host+'/social-api/sys/permission/saveRolePermissions',json=data)
                if admin_res.status_code!=200:
                    raise SystemError('设置权限失败')
                res_json=self.do_request(i)
                if res_json['code'] != 403:
                    print(res_json)
                    print(f'权限校验失败,target:无权限,now:有权限. {i}')
                new_auth_list = copy.deepcopy(auth_list)
                new_auth_list.append(i['id'])
                data = {"roleId": Config.test_user['role_id'], "permissionIds": new_auth_list,
                        "lastPermissionIds": auth_list, "objectPermissions": []}
                admin_res = self.session_admin.post(
                    url=Config.base_host+'/social-api/sys/permission/saveRolePermissions', json=data)
                if admin_res.status_code!=200:
                    raise SystemError('设置权限失败')
                res_json=self.do_request(i)
                if res_json['code'] == 403:
                    print(res_json)
                    print(f'权限校验失败,target:有权限,now:无权限. {i}')

    def do_request(self,i):
        args = {
            'method': i['method'],
            'url': Config.base_host + i['api'],
            'params': i.get('params',{}),
            'json': i.get('body',{})
        }
        if i.get('header', None):
            headers: dict = i.get('header')
            headers.update(self.session_admin.headers)
            args.setdefault('headers', headers)
        res = self.session_tester.request(**args)
        res_json = json.loads(res.text)
        return res_json

    def clean(self):
        pass




if __name__ == '__main__':
    Main().start()
    # t = requests.Session()
    # t.headers.setdefault('Admin-Token', 'cbe8f393c9b7434fa658c4c6f3643bfd')
    # args = {
    #     'method': 'PUT',
    #     'url': Config.base_host + '/social-api/api/channel/tagCategory/edit',
    #     'params': {},
    #     'json': {"id": "1273444722643361794", "name": "test", "children": [
    #                 {"id": "1274222560149561346", "name": "kevin", "type": 2, "categoryId": "1273444722643361794"},
    #                 {"id": "1277438167582040065", "name": "1", "type": 2, "categoryId": "1273444722643361794"},
    #                 {"id": "1277896932286586882", "name": "test", "type": 2, "categoryId": "1273444722643361794"}],
    #                      "type": 1}
    # }
    #
    # res = t.request(**args)
    # print(res.text)