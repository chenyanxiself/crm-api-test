#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:19
# @Author  : yxChen


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 14:24
# @Author  : yxChen

import requests,json,copy,time
from third_auth.config import Config
from third_auth.auth_consts import third_data
import csv

class Main:
    def __init__(self):
        # self.write_header()

        s = requests.Session()
        s.headers.setdefault('Admin-Token', 'e8c00785477e436788659029100badee')
        s.headers.setdefault('Authorization', 'e8c00785477e436788659029100badee')
        self.session_admin: requests.Session=s
        t = requests.Session()
        t.headers.setdefault('Admin-Token', 'c99b63d1d29c4f7c95c006a50026718f')
        t.headers.setdefault('Authorization', 'c99b63d1d29c4f7c95c006a50026718f')
        self.session_tester: requests.Session=t
    def start(self):
        self.domain()
        # self.clean()

    def domain(self):
        #init
        for data in third_data:
            for object in data['objects']:
                for field in object['fields']:
                    print(f'{"-"*5}权限id:{data["permissionId"]}  对象名:{object["name"]}  字段:{field["code"]}  字段名:{field["name"]}{"-"*5}')
                    self.init_field_permission()
                    no_permission_response = self.do_request(object)
                    print('无权限结果'+json.dumps(no_permission_response))

                    self.set_field_permission(data['permissionId'],[field['code']])
                    if self.verify_user_login_permission(data['permissionId'],object['code'],field['code']):
                        print('userLoginPermission权限设置成功')
                        get_permission_response = self.do_request(object)
                        print('有权限结果'+json.dumps(get_permission_response))

                    else:
                        print('userLoginPermission权限设置失败')
                    print(f'{"-"*100}')


    def verify_user_login_permission(self,permission_id,object_code,field_code):
        json_res = self.get_permission()
        for data in json_res['result']:
            if str(data['id'])==str(permission_id):
                for object in data['objects']:
                    if object['code']==object_code:
                        for field in object['fields']:
                            if field['code']==field_code:
                                return field['selected']


    def get_permission(self):
        res = self.session_tester.get(
            url=Config.base_host+'/social-api/sys/user/queryLoginUserPermissions?_t=1594025976').text
        json_res = json.loads(res)
        return json_res

    def init_field_permission(self):
        json_res = self.get_permission()
        objectPermissions = []
        lastPermissionIds = []
        for data in json_res['result']:
            if data['selected'] == True:
                lastPermissionIds.append(data['id'])
            if data.get('objects', None) and not data.get('component', None):
                item = {'permissionId': data['id'], 'objects': []}
                for object in data['objects']:
                    object_item = {'code': object['code'], 'lastFieldCodes': [], 'fieldCodes': []}
                    for field in object['fields']:
                        if field['selected'] == True:
                            object_item['lastFieldCodes'].append(field['code'])
                    item['objects'].append(object_item)
                objectPermissions.append(item)
        json_data = {
            "roleId": "1280045317227601921",
            "permissionIds": Config.second_permission_ids,
            "lastPermissionIds": lastPermissionIds,
            "objectPermissions": objectPermissions
        }
        res=self.session_admin.post(url=Config.base_host+'/social-api/sys/permission/saveRolePermissions', json=json_data)
        print('初始化权限结果: '+res.text)

    def set_field_permission(self,permission_id,fieldCodes):
        json_res = self.get_permission()
        objectPermissions = []
        lastPermissionIds = []
        for data in json_res['result']:
            if data['selected'] == True:
                lastPermissionIds.append(data['id'])
            if data['id']==permission_id:
                item = {'permissionId': data['id'], 'objects': []}
                for object in data['objects']:
                    object_item = {'code': object['code'], 'lastFieldCodes': [], 'fieldCodes': fieldCodes}
                    for field in object['fields']:
                        if field['selected'] == True:
                            object_item['lastFieldCodes'].append(field['code'])
                    item['objects'].append(object_item)
                objectPermissions.append(item)
                break
        json_data = {
            "roleId": "1280045317227601921",
            "permissionIds": Config.second_permission_ids,
            "lastPermissionIds": lastPermissionIds,
            "objectPermissions": objectPermissions
        }
        res=self.session_admin.post(url=Config.base_host + '/social-api/sys/permission/saveRolePermissions', json=json_data)
        print('设置权限结果: ' + res.text)

    def do_request(self,i):
        args = {
            'method': i['method'],
            'url': Config.base_host + i['api'],
            'params': i.get('params',{}),
        }
        if i.get('header', None):
            headers: dict = i.get('header')
            headers.update(self.session_tester.headers)
            args.setdefault('headers', headers)
        content_type = args.get('headers', {}).get('Content-Type', 'application/json')
        if content_type != 'application/json':
            args.setdefault('data', i.get('body',{}))
        else:
            args.setdefault('json', i.get('json',{}))
        res = self.session_tester.request(**args)
        res_json = json.loads(res.text)
        return res_json

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