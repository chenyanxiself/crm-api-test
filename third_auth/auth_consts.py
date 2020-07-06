import requests,json
from third_auth.config import Config

url = 'https://socialapidev2.bjx.cloud/social-api/sys/permission/queryRolePermissions?_t=1594026498&roleId=1275607326874722306'
headers = {'admin-token':'8f38b2df50fa45b9a328889601a11873'}
res = requests.get(url=url,headers=headers).content
res_json = json.loads(res)
list_dict = []
for data in res_json['result']:
    if data.get('objects',None) and not data.get('component',None) :
        for code_data in data['objects']:
            children = []
            children_dict ={}
            for code_fields in code_data['fields']:
                children_dict['code'] = code_fields['code']
                children_dict['name'] = code_fields['name']
                print(children_dict)

#
#
#
# base_data = [
#     {
#         'id':22,
#         'children':[
#             {
#                 'code': 'CHANNEL_LIST',
#                 'api':'',
#                 'children': [
#                     {
#                         {
#                             'code': '1111',
#                             'name': '',
#                         },
#                         {
#                             'code': '2222'
#                         },
#                         {
#                             'code': '3333'
#                         },
#                         {
#                             'code': '4444'
#                         },
#                         {
#                             'code': '5555'
#                         }
#                     },
#                     {
#                 'code': 'CHANNEL_LIST2',
#                 'children': [
#                     {
#                         {
#                             'code': '1111',
#                             'name': '',
#                         },
#                         {
#                             'code': '2222'
#                         },
#                         {
#                             'code': '3333'
#                         },
#                         {
#                             'code': '4444'
#                         },
#                         {
#                             'code': '5555'
#                         }
#                     }
#                 ]
#
#             }
#         ]




