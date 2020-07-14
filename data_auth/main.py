import requests
import json
from data_auth.auth_const import base_data
from data_auth.third_const import third_auths
from data_auth.config import config
class Main():

    def __init__(self):

        s = requests.Session()
        s.headers.setdefault("Admin-Token","c1b4765cacaf4618a166d870d803a3f3")
        s.headers.setdefault("Authorization","c1b4765cacaf4618a166d870d803a3f3")
        self.session_admin:requests.Session= s
        t = requests.Session()
        t.headers.setdefault("Admin-Token", "27feeb3654d34557a6a9ef8e190a4660")
        t.headers.setdefault("Authorization", "27feeb3654d34557a6a9ef8e190a4660")
        self.session_tester: requests.Session = t

    def start(self):
        print("---------------正在执行本部门权限域校验---------------")
        self.domain(base_data,[1,2,3])
        print("---------------正在执行所有子部门权限域校验---------------")
        self.domain(base_data, [1, 2, 4])
        print("---------------正在执行本人权限域校验---------------")
        self.domain(base_data, [1, 2, 701])
    def domain(self,item,auth_list:list):
        for i in item:
            if i.get('children',None):
                auth_list.append(i.get("id"))
                self.domain(i['children'],auth_list)
            else:
                for data in third_auths:
                    for object in data['objects']:
                        self.init_field_permission()
                        print(
                            f'{"-" * 5}权限id:{data["permissionId"]}  对象名:{object["name"]}  字段:{object["code"]}  字段名:{object["name"]}{"-" * 5}')
                        objectPermissions = self.set_field_permission(data['permissionId'],object)
                        auth_res = self.session_admin.get(url = config().base_url+"/social-api/sys/permission/queryRolePermissions",params ={"_t":1594352595,"roleId":config.roleId})
                        if auth_res.status_code != 200:
                            print("角色权限查询失败")
                        lastPermissionIds = []
                        for j in json.loads(auth_res.text)['result']:
                            if j["selected"] == True:
                                lastPermissionIds.append(j)
                        auth_list.append(i['id'])
                        data = {"roleId":"1280045425381924866","permissionIds":auth_list,"lastPermissionIds":lastPermissionIds,"objectPermissions":objectPermissions}
                        admin_res = self.session_admin.post(url=config().base_url+"/social-api/sys/permission/saveRolePermissions",json = data)
                        if admin_res.status_code !=200:
                            print("权限添加失败")
                        res_json = self.do_request(i)
                        print('查询结果'+json.dumps(res_json))
                        parameter = self.regExp_response(i,res_json)
                        creator__department_json = self.response_creator_department(config.creator_deparment_data)
                        if 4 in auth_list:
                            children = self.Department()
                            department:list= self.SubsetsDepartment(children,name=[])
                            department.append(creator__department_json.get("department")[0])
                        else:
                            department:list = (creator__department_json.get("department"))
                        owner =creator__department_json.get("creatorName")
                        for get_permission in parameter:
                            print(get_permission)
                            if get_permission.get('account_company',None):
                                if get_permission.get('account_owner',None):
                                    if isinstance(get_permission.get('account_company', None), list):
                                        department_list = get_permission.get('account_company', None)
                                    else:
                                        department_list: list = []
                                        department_list.append(get_permission.get('account_company', None))
                                    if  len(set(department)&set(department_list)) == 0 and get_permission.get('account_owner',None) != owner:
                                        print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                            elif get_permission.get('departmentName',None):
                                if get_permission.get('creatorName',None):
                                    if isinstance(get_permission.get('departmentName', None), list):
                                        department_list = get_permission.get('departmentName', None)
                                    else:
                                        department_list: list = []
                                        department_list.append(get_permission.get('departmentName', None))
                                    if len(set(department)&set(department_list)) == 0 and get_permission.get('creatorName', None) != owner:
                                        print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")
                            elif get_permission.get('department',None):
                                if get_permission.get('employee_name',None):
                                    if isinstance(get_permission.get('department', None),list):
                                        department_list =get_permission.get('department', None)
                                    else:
                                        department_list:list = []
                                        department_list.append(get_permission.get('department', None))
                                    if len(set(department)&set(department_list)) ==0 and get_permission.get('employee_name', None) != owner:
                                        print(f"权限校验失败，期望值：不能看到其他数据，实际值：能看到其他数据")

                        print("-"*100)
    def regExp_response(self,object,response:dict):
        key_lies = object["objects"].split('.')
        return_value = response
        for key in key_lies:
            return_value = return_value.get(key,None)
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
        res = self.session_tester.request(**args)
        try:
            res_json = json.loads(res.text)
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
if __name__ == "__main__":
    Main().start()