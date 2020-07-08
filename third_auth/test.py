#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:36
# @Author  : yxChen

import requests, json

def get_permission():
    res = requests.get(url='https://socialapidev2.bjx.cloud/social-api/sys/user/queryLoginUserPermissions?_t=1594025976',
                       headers={'admin-token': 'c99b63d1d29c4f7c95c006a50026718f'}).text
    json_res = json.loads(res)
    return json_res


def get_json_data():
    json_res=get_permission()
    result = []
    for data in json_res['result']:
        if data.get('objects', None) and not data.get('component', None):
            item = {'permissionId': data['id'], 'objects': []}
            for object in data['objects']:
                object_item = {'code': object['code'], 'name': object['name'], 'fields': []}
                for field in object['fields']:
                    object_item['fields'].append({'code': field['code'], 'name': field['name']})
                item['objects'].append(object_item)
            result.append(item)
    print(result)

def set_field_permission(fieldCodes:list):
    json_res=get_permission()
    objectPermissions = []
    lastPermissionIds = []
    for data in json_res['result']:
        if data['selected'] == True:
            lastPermissionIds.append(data['id'])
        if data.get('objects', None) and not data.get('component', None):
            item = {'permissionId': data['id'], 'objects': []}
            for object in data['objects']:
                object_item = {'code': object['code'], 'lastFieldCodes': [], 'fieldCodes': fieldCodes}
                for field in object['fields']:
                    if field['selected'] == True:
                        object_item['lastFieldCodes'].append(field['code'])
                item['objects'].append(object_item)
            objectPermissions.append(item)
    json_data = {
        "roleId": "1280045317227601921",
        "permissionIds": ["2","34","802","803","819","3","4","5","701","816","817","822","823","825","1","801","806","807","808","809","804","810","811","820","821","824","818","812","813","814","815","805","50","51","53","49","219","220","221","222","223","224","225","213","215","216","217","218","214","850","1279964091933483009","1279964092382273538","1279964092252250114","1279964092659097601","1279964092797509634","1279964092919144450","1279964093057556482","1279964093200162817","1279964093309214722","1279964093439238146","1279964092537462786","1280032395867922434","1280032396161523713","1280032396291547138","1280032396404793345","1280032396534816769","1280032396656451585","1280032396782280706","1280032396920692738","1280032396044083201","1280032397184933889","1280032397050716161","1280033169431834626","1280033169658327042","1280033169779961857","1280033169909985281","1280033170044203009","1280033170149060610","1280033170266501122","1280033170375553026","1280033169549275137","1280033170597851137","1280033170476216322","114","115","116","117","118","119","120","121","165","167","113","169","170","171","172","173","713","714","123","124","133","130","134","131","135","132","137","136","175","174","144","125","145","126","146","731","127","147","166","730","128","129","140","141","138","142","143","139","168","194","196","195","197","204","198","205","199","206","200","207","201","208","202","209","203","210","732","733","734","6","16","17","18","19","20","15","22","23","24","21","26","27","28","29","30","31","32","33","25","10","11","12","13","8","9","7","728","727"],
        "lastPermissionIds": lastPermissionIds,
        "objectPermissions": objectPermissions
    }
    res=requests.post(url='https://socialapidev2.bjx.cloud/social-api/sys/permission/saveRolePermissions', headers={
        'admin-token': 'e8c00785477e436788659029100badee'
    }, json=json_data)
    print(res.text)


def init_field_permission():
    json_res=get_permission()
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
                    object_item['fieldCodes'].append(field['code'])
                    if field['selected'] == True:
                        object_item['lastFieldCodes'].append(field['code'])
                item['objects'].append(object_item)
            objectPermissions.append(item)
    json_data = {
        "roleId": "1280045317227601921",
        "permissionIds": ["2","34","802","803","819","3","4","5","701","816","817","822","823","825","1","801","806","807","808","809","804","810","811","820","821","824","818","812","813","814","815","805","50","51","53","49","219","220","221","222","223","224","225","213","215","216","217","218","214","850","1279964091933483009","1279964092382273538","1279964092252250114","1279964092659097601","1279964092797509634","1279964092919144450","1279964093057556482","1279964093200162817","1279964093309214722","1279964093439238146","1279964092537462786","1280032395867922434","1280032396161523713","1280032396291547138","1280032396404793345","1280032396534816769","1280032396656451585","1280032396782280706","1280032396920692738","1280032396044083201","1280032397184933889","1280032397050716161","1280033169431834626","1280033169658327042","1280033169779961857","1280033169909985281","1280033170044203009","1280033170149060610","1280033170266501122","1280033170375553026","1280033169549275137","1280033170597851137","1280033170476216322","114","115","116","117","118","119","120","121","165","167","113","169","170","171","172","173","713","714","123","124","133","130","134","131","135","132","137","136","175","174","144","125","145","126","146","731","127","147","166","730","128","129","140","141","138","142","143","139","168","194","196","195","197","204","198","205","199","206","200","207","201","208","202","209","203","210","732","733","734","6","16","17","18","19","20","15","22","23","24","21","26","27","28","29","30","31","32","33","25","10","11","12","13","8","9","7","728","727"],
        "lastPermissionIds": lastPermissionIds,
        "objectPermissions": objectPermissions
    }
    res=requests.post(url='https://socialapidev2.bjx.cloud/social-api/sys/permission/saveRolePermissions', headers={
        'admin-token': 'e8c00785477e436788659029100badee'
    }, json=json_data)
    print(res.text)


# set_field_permission([])
# init_field_permission()

print(isinstance([1,3,4],str))