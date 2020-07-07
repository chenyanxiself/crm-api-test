import requests,json
from third_auth.auth_consts import third_data
import time

class judge_data():
    def __init__(self):
        self.select_fields_code()
    def get_response(self):
        res = requests.get(url="https://socialapidev2.bjx.cloud/social-api/sys/permission/queryRolePermissions?_t=1594102557&roleId=1280045425381924866",headers={'admin-token': '8f38b2df50fa45b9a328889601a11873'}).text
        self.json_res = json.loads(res)
    def select_fields_code(self):
        self.get_response()
        self.now_fields_code = []
        self.lastPermissionIds = []
        for data in self.json_res['result']:
            if data['selected'] == True:
                self.lastPermissionIds.append(data['id'])
            if data.get('objects',None) and not data.get("component",None):
                for object in data['objects']:
                    for fields in object['fields']:
                        if fields['selected'] == True:
                            self.now_fields_code.append(fields["code"])
    def init_field_permission(self,i = third_data[0]):
        headers={"admin-token":"8f38b2df50fa45b9a328889601a11873"}
        lastPermissionIds =self.lastPermissionIds
        permissionIds =["2","34","802","803","819","3","4","5","701","816","817","822","823","825","1","801","806","807","808","809","804","810","811","820","821","824","818","812","813","814","815","805","50","51","53","49","219","220","221","222","223","224","225","213","215","216","217","218","214","850","1279964091933483009","1279964092382273538","1279964092252250114","1279964092659097601","1279964092797509634","1279964092919144450","1279964093057556482","1279964093200162817","1279964093309214722","1279964093439238146","1279964092537462786","1280032395867922434","1280032396161523713","1280032396291547138","1280032396404793345","1280032396534816769","1280032396656451585","1280032396782280706","1280032396920692738","1280032396044083201","1280032397184933889","1280032397050716161","1280033169431834626","1280033169658327042","1280033169779961857","1280033169909985281","1280033170044203009","1280033170149060610","1280033170266501122","1280033170375553026","1280033169549275137","1280033170597851137","1280033170476216322","114","115","116","117","118","119","120","121","165","167","113","169","170","171","172","173","713","714","123","124","133","130","134","131","135","132","137","136","175","174","144","125","145","126","146","731","127","147","166","730","128","129","140","141","138","142","143","139","168","194","196","195","197","204","198","205","199","206","200","207","201","208","202","209","203","210","732","733","734","6","16","17","18","19","20","15","22","23","24","21","26","27","28","29","30","31","32","33","25","10","11","12","13","8","9","7","728","727"]
        objectPermissions ={"permissionId":i["permissionId"],"objects":[]}
        for data in i["objects"]:
            items = {"code":data["code"],"fieldCodes":[],"lastFieldCodes":self.now_fields_code}
            for fieldcodes in data['fields']:
                items['fieldCodes'].append(fieldcodes['code'])
            self.insert_code =items['fieldCodes']
            objectPermissions['objects'].append(items)
        data = {"roleId":"1280045425381924866","lastPermissionIds":lastPermissionIds,"permissionIds":permissionIds,"objectPermissions":objectPermissions}
        res = requests.post(url = "https://socialapidev2.bjx.cloud/social-api/sys/permission/saveRolePermissions",json = data,headers=headers)
        self.select_fields_code()
        if res.status_code == 200:
            if self.now_fields_code == self.insert_code:
                print("权限插入成功")
            else:
                print("权限插入失败")

judge_data().init_field_permission()