#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:24
# @Author  : yxChen

from login import Login
import requests,json,copy,time
from config import Config
from auth_const import list_test_1,list_test_2
import csv

class Main:
    def __init__(self):
        # session_admin = requests.Session()
        # self.session_admin: requests.Session = Login(session_admin, Config.admin_user).get_login_session()
        # session_tester = requests.Session()
        # self.session_tester: requests.Session = Login(session_tester, Config.test_user).get_login_session()
        self.write_header()

        s = requests.Session()
        s.headers.setdefault('Admin-Token', 'd6a54dd39f334172b351b98b502cb6d2')
        s.headers.setdefault('Authorization', 'd6a54dd39f334172b351b98b502cb6d2')
        self.session_admin: requests.Session=s
        t = requests.Session()
        t.headers.setdefault('Admin-Token', 'b5af83b73f964f34b94decfb71b56f35')
        s.headers.setdefault('Authorization', 'b5af83b73f964f34b94decfb71b56f35')
        self.session_tester: requests.Session=t

    def start(self):
        self.domain(list_test_1,["3", "4", "5", "701", "2"])
        self.customer_business(list_test_2, ["3", "4", "5", "701", "2"])
        self.clean()

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
                        lastPermissionIds.append(j['id'])
                data = {"roleId":Config.test_user['role_id'],"permissionIds":auth_list,"lastPermissionIds":lastPermissionIds,"objectPermissions":[]}
                admin_res = self.session_admin.post(url=Config.base_host+'/social-api/sys/permission/saveRolePermissions',json=data)
                if admin_res.status_code!=200:
                    raise SystemError('设置权限失败')
                res_json=self.do_request(i)
                if res_json['code'] != 403:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': False, '期望值': '无权限',
                         '实际值': '有权限'}]
                    self.write_row(rows)
                    print(f'权限校验失败,target:无权限,now:有权限. {i}')
                else:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': True, '期望值': '无权限',
                         '实际值': '无权限'}]
                    self.write_row(rows)
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
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': False, '期望值': '有权限',
                         '实际值': '无权限'}]
                    self.write_row(rows)
                    print(f'权限校验失败,target:有权限,now:无权限. {i}')
                else:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': True, '期望值': '有权限',
                         '实际值': '有权限'}]
                    self.write_row(rows)

    def customer_business(self,item,auth_list:list):
        for i in item:
            if i.get('children',None):
                auth_list.append(i['id'])
                self.customer_business(i['children'],auth_list)
            else:
                auth_res = self.session_admin.get(url=Config.base_host+'/social-api/sys/permission/queryRolePermissions',
                                 params={'_t': 1593591992, 'roleId': Config.test_user['role_id']})
                lastPermissionIds = []
                if auth_res.status_code!=200:
                    raise SystemError('获取权限列表失败')
                for j in json.loads(auth_res.text)['result']:
                    if j['selected'] == True:
                        lastPermissionIds.append(j['id'])
                data = {"roleId":Config.test_user['role_id'],"permissionIds":auth_list,"lastPermissionIds":lastPermissionIds,"objectPermissions":[]}
                admin_res = self.session_admin.post(url=Config.base_host+'/social-api/sys/permission/saveRolePermissions',json=data)

                if admin_res.status_code!=200:
                    raise SystemError('设置权限失败')
                res_json=self.do_request(i)

                if res_json.get('code',None) != 500:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': False, '期望值':'无权限','实际值':'有权限'}]
                    self.write_row(rows)
                    # print(res_json)
                    print(f'权限校验失败,target:无权限,now:有权限. {i}')
                else:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': True, '期望值': '无权限',
                         '实际值': '无权限'}]
                    self.write_row(rows)
                new_auth_list = copy.deepcopy(auth_list)
                new_auth_list.append(i['id'])
                data = {"roleId": Config.test_user['role_id'], "permissionIds": new_auth_list,
                        "lastPermissionIds": auth_list, "objectPermissions": []}
                admin_res = self.session_admin.post(
                    url=Config.base_host+'/social-api/sys/permission/saveRolePermissions', json=data)
                if admin_res.status_code!=200:
                    raise SystemError('设置权限失败')
                res_json=self.do_request(i)
                if res_json.get('code',None) == 500:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': False, '期望值': '有权限',
                         '实际值': '无权限'}]
                    self.write_row(rows)
                    print(f'权限校验失败,target:有权限,now:无权限. {i}')
                else:
                    rows = [
                        {'接口名': i['name'], '接口id': i['id'], '接口url': i['api'],
                         '接口所有内容': str(i), '返回状态码': res_json['code'], '返回内容': res_json, '测试是否通过': True, '期望值': '有权限',
                         '实际值': '有权限'}]
                    self.write_row(rows)



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
        try:

            res_json = json.loads(res.text)
            return res_json
        except:
            return {'code':500}

    def write_header(self):
        self.csvs = open(f'{str(int(time.time()))}.csv','w',newline='')
        headers: list = ['接口名', '接口id', '接口url', '接口所有内容', '返回状态码', '返回内容', '测试是否通过', '期望值', '实际值']
        self.writes = csv.DictWriter(self.csvs, headers)
        self.writes.writeheader()

    def write_row(self,rows:list):
        self.writes.writerows(rows)

    def clean(self):
        self.csvs.close()




if __name__ == '__main__':
    Main().start()
    # t = requests.Session()
    # t.headers.setdefault('Admin-Token', 'cbe8f393c9b7434fa658c4c6f3643bfd')
    # args = {
    #     'method': 'GET',
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