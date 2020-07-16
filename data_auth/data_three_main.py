import requests
import json
from data_auth.third_const import third_auths
from data_auth.config import config
import csv
import time
class Main_Permission_three_domain():

    def __init__(self):
        self.write_header()
        s = requests.Session()
        s.headers.setdefault("Admin-Token","c1b4765cacaf4618a166d870d803a3f3")
        s.headers.setdefault("Authorization","c1b4765cacaf4618a166d870d803a3f3")
        self.session_admin:requests.Session= s
        t = requests.Session()
        t.headers.setdefault("Admin-Token", "c4e67dca65514f19b1033e71ec0954f9")
        t.headers.setdefault("Authorization", "c4e67dca65514f19b1033e71ec0954f9")
        self.session_tester: requests.Session = t

    def start(self):
        self.domain( [1, 2])
        self.domain([1,2,3])
        self.domain( [1, 2, 4])
        self.domain([1, 2, 701])
        self.clean()
    def domain(self,auth_list:list):
        #测试权限域三级权限
        for datas in third_auths:
            print(datas)
            for object in datas['objects']:
                # self.init_field_permission() 清除权限
                self.init_field_permission()
                print(f'{"-" * 5}权限id:{datas["permissionId"]}  对象名:{object["name"]}  字段:{object["code"]}  字段名:{object["name"]}{"-" * 5}')
                #获取上次三级权限
                objectPermissions = self.set_field_permission(datas['permissionId'], object)
                #获取上次二级权限
                auth_res = self.session_admin.get(
                    url=config().base_url + "/social-api/sys/permission/queryRolePermissions",
                    params={"_t": 1594352595, "roleId": config.roleId})
                if auth_res.status_code != 200:
                    print("角色权限查询失败")
                lastPermissionIds = []
                for j in json.loads(auth_res.text)['result']:
                    if j["selected"] == True:
                        lastPermissionIds.append(j)
                #添加本次测试所有一二级权限ID
                auth_list.extend(config.second_permission_ids)
                data = {"roleId": "1280045425381924866", "permissionIds": auth_list,
                        "lastPermissionIds": lastPermissionIds, "objectPermissions": objectPermissions}
                admin_res = self.session_admin.post(
                    url=config().base_url + "/social-api/sys/permission/saveRolePermissions", json=data)
                if admin_res.status_code != 200:
                    print("权限添加失败")
                res_json = self.do_request(object)
                # print('查询结果'+json.dumps(res_json))
                parameter = self.regExp_response(object, res_json)
                creator__department_json = self.response_creator_department(config.creator_deparment_data)
                if 4 in auth_list:
                    data_auto = True
                    print(f'{"-" * 20}正在做所有子部门数据域权限校验{"-" * 20}')
                    children = self.Department()
                    department: list = self.SubsetsDepartment(children, name=[])
                    department.append(creator__department_json.get("department")[0])
                    owner = creator__department_json.get("creatorName")
                    for get_permission in parameter:
                        print(get_permission)
                        if get_permission.get('account_company', None):
                            if get_permission.get('account_owner', None):
                                if isinstance(get_permission.get('account_company', None), list):
                                    department_list = get_permission.get('account_company', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('account_company', None))
                                if len(set(department) & set(department_list)) == 0 and get_permission.get(
                                        'account_owner', None) != owner:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        elif get_permission.get('departmentName', None):
                            if get_permission.get('creatorName', None):
                                if isinstance(get_permission.get('departmentName', None), list):
                                    department_list = get_permission.get('departmentName', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('departmentName', None))
                                if len(set(department) & set(department_list)) == 0 and get_permission.get(
                                        'creatorName', None) != owner:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")

                        elif get_permission.get('department', None):
                            if get_permission.get('employee_name', None):
                                if isinstance(get_permission.get('department', None), list):
                                    department_list = get_permission.get('department', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('department', None))
                                if len(set(department) & set(department_list)) == 0 and get_permission.get(
                                        'employee_name', None) != owner:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                    if data_auto == False:
                        rows = [{'当前数据域': '所有子部门', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': False, '期望值': False, '实际值': True}]
                        self.write_row(rows)
                    else:
                        rows = [{'当前数据域': '所有子部门', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': True, '期望值': False, '实际值': False}]
                        self.write_row(rows)
                elif 3 in auth_list:
                    data_auto = True
                    print(f'{"-" * 20}正在做本部门数据域权限校验{"-" * 20}')
                    department: list = (creator__department_json.get("department"))
                    for get_permission in parameter:
                        print(get_permission)
                        if get_permission.get('account_company', None):
                            if get_permission.get('account_owner', None):
                                if isinstance(get_permission.get('account_company', None), list):
                                    department_list = get_permission.get('account_company', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('account_company', None))
                                if len(set(department) & set(department_list)) == 0:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        elif get_permission.get('departmentName', None):
                            if get_permission.get('creatorName', None):
                                if isinstance(get_permission.get('departmentName', None), list):
                                    department_list = get_permission.get('departmentName', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('departmentName', None))
                                if len(set(department) & set(department_list)) == 0:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        elif get_permission.get('department', None):
                            if get_permission.get('employee_name', None):
                                if isinstance(get_permission.get('department', None), list):
                                    department_list = get_permission.get('department', None)
                                else:
                                    department_list: list = []
                                    department_list.append(get_permission.get('department', None))
                                if len(set(department) & set(department_list)) == 0:
                                    data_auto = False
                                    print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                    if data_auto == False:
                        rows = [{'当前数据域': '本部门', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': False, '期望值': False, '实际值': True}]
                        self.write_row(rows)
                    else:
                        rows = [{'当前数据域': '本部门', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': True, '期望值': False, '实际值': False}]
                        self.write_row(rows)
                elif 701 in auth_list:
                    data_auto = True
                    print(f'{"-" * 20}正在做本人数据域权限校验{"-" * 20}')
                    owner = creator__department_json.get("creatorName")
                    for get_permission in parameter:
                        print(get_permission)
                        if get_permission.get('account_owner', None):
                            if get_permission.get('account_owner', None) != owner:
                                data_auto = False
                                print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        if get_permission.get('creatorName', None):
                            if get_permission.get('creatorName', None) != owner:
                                data_auto = False
                                print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        if get_permission.get('employee_name', None):
                            if get_permission.get('employee_name', None) != owner:
                                data_auto = False
                                print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                    if data_auto == False:
                        rows = [{'当前数据域': '本人', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': False, '期望值': False, '实际值': True}]
                        self.write_row(rows)
                    else:
                        rows = [{'当前数据域': '本人', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': True, '期望值': False, '实际值': False}]
                        self.write_row(rows)
                else:
                    data_auto = True
                    print(f'{"-" * 20}正在做无数据域权限校验{"-" * 20}')
                    for get_permission in parameter:
                        # print(get_permission)
                        if get_permission.get('account_company') not in ('', None) or get_permission.get(
                                'account_owner') not in ("", None):
                            data_auto = False
                            # print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        elif get_permission.get('departmentName') not in ('', None) or get_permission.get(
                                'creatorName') not in ("", None):
                            data_auto = False
                            # print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                        elif get_permission.get('department') not in ("", None) or get_permission.get(
                                'employee_name') not in ("", None):
                            data_auto = False
                            # print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                    if data_auto == False:
                        rows = [{'当前数据域': '无数据域', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': False, '期望值': False, '实际值': True}]
                        self.write_row(rows)
                    else:
                        rows = [{'当前数据域': '无数据域', '字段名': object["name"], '字段ID': object["code"],
                                 '父级权限ID': datas["permissionId"],
                                 '接口url': object['api'], '接口所有内容': data,
                                 '返回状态码': res_json['code'], '返回内容': res_json,
                                 '测试是否通过': True, '期望值': False, '实际值': False}]
                        self.write_row(rows)
                print("-" * 100)



    def regExp_response(self,object,response:dict):
        key_lies = object["objects"].split('.')
        print(key_lies)
        return_value = response
        for key in key_lies:
            return_value = return_value.get(key,None)
            print(return_value)
            if return_value == None:
                return return_value
        return return_value

    def response_creator_department(self,object):
        args = {
            "url": config().base_url + object["url"],
            "method": object["method"],
            'params': object.get('params', {}),
        }
        res = self.session_admin.request(**args)
        res_json = json.loads(res.text)
        roleid_list = []
        for data in res_json['result']['records']:
            if data.get('roleIds', None):
                if data.get('roleIds', None)[0].get('id', None):
                    if config.roleId == data.get('roleIds', None)[0].get('id', None):
                        res_dict: dict = {"creatorName": "", "department": []}
                        res_dict['creatorName'] = data['creatorName']
                        if data.get('departIds', None):
                            for departments in data.get('departIds'):
                                res_dict.get("department").append(departments.get('name'))
                        else:
                            res_dict.get("department").append(None)
                        roleid_list.append(res_dict)
        return roleid_list[0]

    def get_permission(self):
        res = self.session_tester.get(
            url=config.base_url+'/social-api/sys/user/queryLoginUserPermissions?_t=1594025976&roleId=1280045425381924866').text
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
            "roleId": "1280045425381924866",
            "permissionIds":[1,2],
            "lastPermissionIds": lastPermissionIds,
            "objectPermissions": objectPermissions
        }
        res=self.session_admin.post(url=config.base_url+'/social-api/sys/permission/saveRolePermissions', json=json_data)
        print('初始化权限结果: '+res.text)

    def set_field_permission(self,permissionId,object):
            test_lastFieldCodes = self.get_permission()
            for result in test_lastFieldCodes.get("result"):
                objectPermissions = {"permissionId": permissionId,"objects": {"code": object['code'], "lastFieldCodes": [], "fieldCodes": []}}
                if result.get("id") == permissionId:
                    for object_result in result.get("objects"):
                        if object_result.get("fields", None):
                            lastFieldCodes = []
                            for field in object_result.get("fields", None):
                                if field["selected"] == True:
                                    lastFieldCodes.append(field['code'])
                                objectPermissions["lastFieldCodes"] = lastFieldCodes
                objectPermissions.get("objects")['fieldCodes'] = object.get("fields")[0].get("code")
            return objectPermissions

    def do_request(self,i):
        args ={
            "url":config().base_url+i["api"],
            "method":i["method"],
            'params': i.get('params',{}),
        }
        if i.get("headers",None):
            headers:dict = i.get("headers")
            headers.update(self.session_tester.headers)
            args.setdefault("headers",headers)
        content_type = args.get("headers",{}).get('content_type',"application/json")
        if content_type != "application/json":
            args.setdefault("data",i.get("body",{}))
        else:
            args.setdefault("json",i.get("body",{}))
        print("-"*50)
        print(args)
        print("-"*50)

        res = self.session_tester.request(**args)
        print(res.status_code)
        try:
            res_json = json.loads(res.text)
            print(res_json)
            return res_json
        except:
            return {"code":500}

    def Department(self):
        url = config.base_url + "/social-api/sys/role/departRole?_t=1594611172"
        res = self.session_admin.get(url=url).text
        res_json = json.loads(res)
        for data in res_json["result"]:
            if data.get("title") == "测试部门":
                return data
    def SubsetsDepartment(self,children, name):
        if children.get("children", None) != []:
            if isinstance(children.get('children'), list):
                name.append(children.get("children")[0].get('title'))
                children_list = children.get("children")[0]
                return self.SubsetsDepartment(children_list, name)
        else:
            return name
    def write_header(self):
        self.csvs = open(f'{str(int(time.time()))}.csv','w',newline='')
        headers: list = ['当前数据域','字段名', '字段ID', '父级权限ID', '接口url', '接口所有内容', '返回状态码', '返回内容', '测试是否通过', '期望值', '实际值']
        self.writes = csv.DictWriter(self.csvs, headers)
        self.writes.writeheader()

    def write_row(self,rows:list):
        self.writes.writerows(rows)
    def clean(self):
        self.csvs.close()
if __name__ == "__main__":
    Main_Permission_three_domain().start()