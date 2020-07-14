import requests,json
from data_auth.third_const import third_auths
from data_auth.config import config


def Department():
    url = "https://socialapidev2.bjx.cloud/social-api/sys/role/departRole?_t=1594611172"
    headers = {"Admin-Token":"c1b4765cacaf4618a166d870d803a3f3"}
    res = requests.get(url=url,headers=headers).content
    res_json = json.loads(res)
    for data in res_json["result"]:
        if data.get("title") == "测试部门":
            print(data)
            return data
def SubsetsDepartment(children,name):
    if children.get("children",None) != []:
        if isinstance(children.get('children'),list):
            name.append(children.get("children")[0].get('title'))
            canshu = children.get("children")[0]
            SubsetsDepartment(canshu, name)
    else:
        return name
res_json  = Department()
SubsetsDepartment(res_json,name=[])
# def get_permission():
#     headers = {"admin-token": "a0e908303d4c4d0f939eadc2e4b64ab9"}
#     res = requests.get(
#         url=config.base_url + '/social-api/sys/permission/queryRolePermissions?_t=1594376881&roleId=1280045425381924866',headers = headers).text
#     json_res = json.loads(res)
#     return json_res

# for data in third_auths:
#     permissionId = data.get("permissionId")
#     for object in data['objects']:
#         test_lastFieldCodes = get_permission()
#         for result in test_lastFieldCodes.get("result"):
#             objectPermissions = {"permissionId": permissionId,"objects": {"code": object['code'], "lastFieldCodes": [],"fieldCodes": []}}
#             if result.get("id") == permissionId:
#                 for object_result in result.get("objects"):
#                     if object_result.get("fields",None):
#                         lastFieldCodes = []
#                         for field in object_result.get("fields",None):
#                             if field["selected"] == True:
#                                 lastFieldCodes.append(field['code'])
#                         objectPermissions["lastFieldCodes"] = lastFieldCodes
#             objectPermissions['fieldCodes'] = object.get("fields")[0].get("code")
#     print(objectPermissions)




# url = "https://socialapidev2.bjx.cloud/social-api/sys/permission/saveRolePermissions"
#
#
#
# lastPermissionIds =["1","2"]
# permissionIds = ["1", "2", "3", "4", "701"]
# data = {"roleId":"1280045425381924866","lastPermissionIds":lastPermissionIds,"permissionIds":permissionIds,"objectPermissions":[]}
# headers={"admin-token":"8f38b2df50fa45b9a328889601a11873"}
# res = requests.post(url=url,json=data,headers=headers).content.decode("utf-8")
# print(res)

# test = {
#     "headers1":"sssss"
# }
#
# a=test.get("headers", {})
# print(a)

# url = "https://socialapidev2.bjx.cloud/social-api/sys/user/list"
# params = {"_t":1594361522,"column":"createTime","order":"desc","field":"id,,,realname,workNo,avatar,undefined,undefined,undefined,creatorName,createTime,action","pageNo":1,"pageSize":20}
# headers = {"admin-token":"a0e908303d4c4d0f939eadc2e4b64ab9"}
# res = requests.get(url=url,params =params,headers = headers).text
# res_json = json.loads(res)
# roleid_list = []
# for data in res_json['result']['records']:
#     if data.get('roleIds',None):
#         if data.get('roleIds',None)[0].get('id',None):
#             if "1280045425381924866" == data.get('roleIds', None)[0].get('id', None):
#                 res_dict: dict = {"creatorName": "", "department": []}
#                 res_dict['creatorName'] = data['creatorName']
#                 if data.get('departIds', None):
#                     for departments in data.get('departIds'):
#                         res_dict.get("department").append(departments.get('name'))
#                 else:
#                     res_dict.get("department").append(None)
#                 roleid_list.append(res_dict)
