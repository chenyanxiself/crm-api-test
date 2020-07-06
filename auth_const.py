#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 10:37
# @Author  : yxChen


base_data = [
    {
        'id': 803,
        'name': '市场资源',
        'children': [
            {
                'id': 801,
                'name': '账号组资源',
                'children': [
                    {
                        'id': 804,
                        'name': '账号组资源汇总',
                        'children': [
                            {
                                'id': 806,
                                'name': '查看汇总数据',
                                'api': '/social-api/api/channel/channelTableProperty/accountGroupSummarizeList',
                                'method': 'POST',
                                'params': {},
                                'body': {"column": "createTime", "order": "desc", "field": "id,", "pageNo": 1,
                                         "pageSize": 20},
                            },
                            {
                                'id': 807,
                                'name': '编辑汇总数据',
                                'api': '/social-api/api/channel/channelTableValue/accountGroupCollectEdit',
                                'method': 'PUT',
                                'params': {},
                                'body': {"tableId": "1273918310894854146",
                                         "importInfo": {"applicant_company": "af956d2bad344012812b3df72fb0b989",
                                                        "applicant": "", "approver_company": "", "examination": "",
                                                        "registrant": "", "account_type": "测试1", "account": "123",
                                                        "password": "123", "binding_phone": "123",
                                                        "account_company": "", "account_owner": ""},
                                         "id": "1273918541250224129"},
                            },
                            {
                                'id': 808,
                                'name': '删除汇总数据',
                                'api': '/social-api/api/channel/channelTableValue/accountGroupCollectDelete/95986',
                                'method': 'DELETE',
                                'params': {},
                                'body': {},
                            },
                            {
                                'id': 809,
                                'name': '查看报表统计',
                                'api': '/social-api/api/channel/statistical/accountGroup/overview?_t=1593503484&channelFlag=2',
                                'method': 'GET',
                                'params': {},
                                'body': {},

                            }
                        ]
                    },
                    {
                        'id': 818,
                        'name': '账号组管理',
                        'children': [
                            {
                                'id': 810,
                                'name': '查看账号组列表',
                                'api': '/social-api/api/channel/channel/queryAccountGroup',
                                'method': 'POST',
                                'params': {},
                                'body': {"channelFlag": 2, "column": "createTime", "order": "desc",
                                         "field": "id,,channelCode,channelName,creatorName,createTime,status,departmentName,action",
                                         "pageNo": 1, "pageSize": 20},
                            },
                            {
                                'id': 811,
                                'name': '编辑',
                                'api': '/social-api/api/channel/channel/editAccountGroup',
                                'method': 'POST',
                                'params': {},
                                'body': {"channelFlag": 2, "name": "测试权限", "code": "CSQX",
                                         "departmentId": ["af956d2bad344012812b3df72fb0b989"],
                                         "id": "1277424729371762689"},

                            },
                            {
                                'id': 820,
                                'name': '启用',
                                'api': '/social-api/api/channel/channel/enabledAccountGroup',
                                'method': 'POST',
                                'params': {},
                                'body': {"id": "1277424729371762689"},
                            },
                            {
                                'id': 821,
                                'name': '禁用',
                                'api': '/social-api/api/channel/channel/disabledAccountGroup',
                                'method': 'POST',
                                'params': {},
                                'body': {"id": "1277424729371762689"},
                            }
                        ]
                    },

                ]
            },
            {
                'id': 802,
                'name': '渠道客户资源',
                'children': [
                    {
                        'id': 805,
                        'name': '渠道客户资源汇总',
                        'children': [
                            {
                                'id': 812,
                                'name': '查看汇总数据',
                                'api': '/social-api/api/channel/channelTableProperty/channelAccountSummarizelist',
                                'method': 'POST',
                                'params': {},
                                'body': {"column": "createTime", "order": "desc", "field": "id,", "pageNo": 1,
                                         "pageSize": 20}
                            },
                            {
                                'id': 813,
                                'name': '编辑汇总数据',
                                'api': '/social-api/api/channel/channelTableValue/channelAccountCollectEdit',
                                'method': 'PUT',
                                'params': {},
                                'body': {"tableId": "1273918904531476481",
                                         "importInfo": {"department": "db83e1f4548f4397814ad3a63b94a0d1",
                                                        "employee_name": "47", "position": "1", "game_account": "111",
                                                        "customer_name": "111", "mobile_phone": "1111198484161",
                                                        "wechat": "", "email": "", "hey_hey": "", "weibo": "",
                                                        "tieba": "", "trill": "", "quick_worker": ""},
                                         "id": "1274988117446680578"}
                            },
                            {
                                'id': 814,
                                'name': '删除汇总数据',
                                'api': '/social-api/api/channel/channelTableValue/delete/9895',
                                'method': 'DELETE',
                                'params': {},
                                'body': {}
                            },
                            {
                                'id': 815,
                                'name': '查看报表统计',
                                'api': '/social-api/api/channel/statistical/channelGroup/overview?_t=1593506443&channelFlag=1',
                                'method': 'GET',
                                'params': {},
                                'body': {}
                            }
                        ]
                    },
                    {
                        'id': 819,
                        'name': '渠道管理',
                        'children': [
                            {
                                'id': 816,
                                'name': '查看渠道列表',
                                'method': 'POST',
                                'api': '/social-api/api/channel/channel/queryChannelAccount',
                                'params': {},
                                'body': {"channelFlag": 1, "column": "createTime", "order": "desc",
                                         "field": "id,,channelCode,channelName,creatorName,createTime,status,departmentName,action",
                                         "pageNo": 1, "pageSize": 20}
                            },
                            {
                                'id': 817,
                                'name': '编辑',
                                'method': 'POST',
                                'api': '/social-api/api/channel/channel/editAccountGroup',
                                'params': {},
                                'body': {"channelFlag": 1, "name": "测试", "code": "CS",
                                         "departmentId": ["c82826768f644be8be737c2bdd2952aa"],
                                         "id": "1277886208147513345"}
                            },
                            {
                                'id': 822,
                                'name': '启用',
                                'method': 'POST',
                                'api': '/social-api/api/channel/channel/enabledChannel',
                                'params': {},
                                'body': {"id": "1277886208147513345"}
                            },
                            {
                                'id': 823,
                                'name': '禁用',
                                'method': 'POST',
                                'api': '/social-api/api/channel/channel/disabledChannel',
                                'params': {},
                                'body': {"id": "1277886208147513345"}
                            },
                            {
                                'id': 825,
                                'name': '新建',
                                'method': 'POST',
                                'api': '/social-api/api/channel/channel/add',
                                'params': {},
                                'body': {"channelFlag": 1, "name": "测试1", "code": "CS",
                                         "departmentId": ["0380db65f79c422a948f8b2fafd2bc0c",
                                                          "23b1dfc40cba4a44aafe3a69e0e3ef6b"]}
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        'id': 49,
        'name': '导入数据任务',
        'children': [
            {
                'id': 50,
                'name': '查看导入任务列表',
                'api': '/social-api/api/crm/importTask/select',
                'method': 'POST',
                'params': {},
                'body': {"importObjectId": "0", "channelId": "0", "column": "createTime", "order": "desc",
                         "field": "id,,,fileName,totalCount,undefined,undefined,finishMsg,departmentName,creatorName,tableName,createTime,action",
                         "pageNo": 1, "pageSize": 20}
            },
            {
                'id': 51,
                'name': '查看导入任务明细',
                'api': '/social-api/api/crm/importTaskInfo/list',
                'method': 'POST',
                'params': {},
                'body': {"column": "createTime", "order": "desc", "field": "id,", "pageNo": 1, "pageSize": 20,
                         "importTaskId": "1274232437353799682", "importObjectId": "1273825050318921729"}
            },
            {
                'id': 53,
                'name': '下载失败数据',
                'api': '/social-api/api/crm/importTaskInfo/export',
                'method': 'POST',
                'params': {},
                'body': {"id": "1274231682647517"}
            }
        ]
    },
    {
        'id': 213,
        'name': '标签管理设置',
        'children': [
            {
                'id': 219,
                'name': '查看标签',
                'api': '/social-api/api/channel/tagCategory/tree',
                'method': 'POST',
                'params': {},
                'body': {}
            },
            {
                'id': 220,
                'name': '创建标签',
                'api': '/social-api/api/channel/tag/add',
                'method': 'POST',
                'params': {},
                'body': {"name": "test", "categoryId": "1273444722643361794"}
            },
            {
                'id': 221,
                'name': '编辑标签',
                'api': '/social-api/api/channel/tag/edit',
                'method': 'PUT',
                'params': {},
                'body': {"id":"12","name":"1","type":2,"categoryId":"1"}
            },
            {
                'id': 222,
                'name': '删除标签',
                'api': '/social-api/api/channel/tag/delete?id=1277896932286586882',
                'method': 'DELETE',
                'params': {'id': '1277896932286586882'},
                'body': {}
            },
            {
                'id': 223,
                'name': '编辑标签分类',
                'api': '/social-api/api/channel/tagCategory/edit',
                'method': 'PUT',
                'params': {},
                'body': {"id": "1273444722643361794", "name": "test", "children": [
                    {"id": "1274222560149561346", "name": "kevin", "type": 2, "categoryId": "1273444722643361794"},
                    {"id": "1277438167582040065", "name": "1", "type": 2, "categoryId": "1273444722643361794"}],
                         "type": 1}
            },
            {
                'id': 224,
                'name': '创建标签分类',
                'api': '/social-api/api/channel/tagCategory/add',
                'method': 'POST',
                'params': {},
                'body': {"name": "test"}
            },
            {
                'id': 225,
                'name': '删除标签分类',
                'api': '/social-api/api/channel/tagCategory/delete?id=1277898581335924738',
                'method': 'DELETE',
                'params': {},
                'body': {}
            }
        ]
    },
    {
        'id': 214,
        'name': '产品设置',
        'children': [
            {
                'id': 215,
                'name': '查看产品',
                'api': '/social-api/api/channel/product/list',
                'method': 'POST',
                'params': {},
                'body': {"column": "createTime", "order": "desc", "field": "id,,,name,creatorName,createTime,action",
                         "pageNo": 1, "pageSize": 20}
            },
            {
                'id': 216,
                'name': '创建产品',
                'api': '/social-api/api/channel/product/add',
                'method': 'POST',
                'params': {},
                'body': {"name": "test"}
            },
            {
                'id': 217,
                'name': '编辑产品',
                'api': '/social-api/api/channel/product/edit',
                'method': 'PUT',
                'params': {},
                'body': {"createTime": "2020-05-01 00:01:18", "creator": "13", "creatorName": "冯十一", "delFlag": 2,
                         "id": "1255889975163518977", "name": "产品b", "status": 1}
            },
            {
                'id': 218,
                'name': '查看产品',
                'api': '/social-api/api/channel/product/delete?id=1277900893739606017',
                'method': 'DELETE',
                'params': {'id': '1277900893739606017'},
                'body': {}
            }
        ]
    }
]

customer_data = [
    {
        'id': 123,
        'name': '工作台',
        'children': [
            {
                'id':169,
                'name':'查看新增线索',
                'api':'/CrmBackLog/todayLeads',
                'method':'POST',
                'params':{},
                'body':{"page":1,"limit":15,"search":"","type":4,"isSub":1,"label":2}
            },{
                'id':170,
                'name':'查看新增客户',
                'api':'/CrmBackLog/todayCustomer',
                'method':'POST',
                'params':{},
                'body':{"page":1,"limit":15,"search":"","type":5,"isSub":1,"label":2}
            },{
                'id':171,
                'name':'查看新增跟进记录',
                'api':'/Crm/Instrument/queryRecordConunt',
                'method':'POST',
                'params':{},
                'body':{"page":1,"limit":15,"search":"","type":4,"isSub":1,"label":2}
            },{
                'id':172,
                'name':'查看逾期未联系客户',
                'api':'/CrmBackLog/todayCustomer',
                'method':'POST',
                'params':{},
                'body':{"page":1,"limit":15,"search":"","type":2,"isSub":1,"label":2}
            },{
                'id':173,
                'name':'查看逾期未联系线索',
                'api':'/CrmBackLog/todayLeads',
                'method':'POST',
                'params':{},
                'body':{"page":1,"limit":15,"search":"","type":2,"isSub":1,"label":2}
            },{
                'id':713,
                'name':'客户转化阶段漏斗',
                'api':'/biCustomer/convertcus',
                'method':'POST',
                'params':{},
                'body':{"startTime":"2020-06-30 00:00:00","endTime":"2020-06-30 23:59:59","creator":"73"},
                'header':{'Content-Type':'application/x-www-form-urlencoded'}
            },{
                'id':714,
                'name':'新增客户跟进状态漏斗',
                'api':'/biCustomer/cusfollow',
                'method':'POST',
                'params':{},
                'body':{"startTime":"2020-06-30 00:00:00","endTime":"2020-06-30 23:59:59","creator":"73"},
                'header':{'Content-Type':'application/x-www-form-urlencoded'}
            },
        ]
    },
    {
        'id':124,
        'name':'待办事项',
        'children':[
            {
                'id':130,
                'name':'今日需联系线索',
                'children':[
                    {
                        'id': 133,
                        'name': "查看今日需联系线索",
                        'api': "/CrmBackLog/todayLeads",
                        'method': "POST",
                        'params': "",
                        'body': {"page":1,"limit":15,"isSub":1,"type":1}
                    }
                ]
            },
            {
                'id':131,
                'name':'今日需联系客户',
                'children':[
                    {
                        'id':134,
                        'name':'查看今日需联系客户',
                        'api':"/CrmBackLog/todayCustomer",
                        'method':"POST",
                        'params':{},
                        'body':{"page":1,"limit":15,"isSub":1,"type":2}
                    }

                ]
            },
            {
                'id':132,
                'name':'分配给我的线索',
                'children':[
                    {
                        'id':135,
                        'name':'查看分配给我的线索',
                        'api':"/CrmBackLog/followLeads",
                        'method':"POST",
                        'params':{},
                        'body':{"page":1,"limit":15,"isSub":1,"type":2}
                    }

                ]
            },{
                'id':136,
                'name':'我的客户',
                'children':[
                    {
                        'id':137,
                        'name':'查看分配给我的客户',
                        'api':"/CrmBackLog/followCustomer",
                        'method':"POST",
                        'params':{},
                        'body':{"page":1,"limit":15,"isSub":1,"type":2}
                    }

                ]
            },{
                'id':174,
                'name':'查看待进公海客户',
                'children':[
                    {
                        'id':175,
                        'name':'查看待进公海客户',
                        'api':"/CrmBackLog/putInPoolRemind",
                        'method':"POST",
                        'params':{},
                        'body':{"page":1,"limit":15,"isSub":1,"type":2}
                    }

                ]
            }
        ]
    },
    {
        'id':125,
        'name':'线索',
        'children':[
            {
                'id': 144,
                'name': "查看线索列表",
                'api': "/CrmLeads/queryPageList",
                'method': "POST",
                'params': "",
                'body': {"page":2,"limit":15,"search":"","type":1}
            }
        ]
    },
    {
        'id':126,
        'name':'客户',
        'children':[
            {
                'id': 145,
                'name': "查看客户列表",
                'api': "/CrmCustomer/queryPageList",
                'method': "POST",
                'params': "",
                'body': {"page":1,"limit":15,"search":"","type":2}
            }
        ]
    },
    {
        'id':127,
        'name':'公海',
        'children':[
            {
                'id': 146,
                'name': "查看公海列表",
                'api': "/CrmCustomer/queryPoolPageList",
                'method': "POST",
                'params': "",
                'body': {"page":2,"limit":15,"search":"","type":9}
            },
            {
                'id': 731,
                'name': "公海领取",
                'api': "/CrmCustomer/receiveByIds",
                'method': "POST",
                'params': "",
                'body': {"ids":38},
                'header':{'Content-Type':'application/x-www-form-urlencoded'}
            }
        ]
    },
    {
        'id':128,
        'name':'死海',
        'children':[
            {
                'id': 147,
                'name': "查看死海列表",
                'api': "/CrmCustomer/queryPoolPageList",
                'method': "POST",
                'params': "",
                'body': {"page":1,"limit":15,"search":"","type":10}
            },{
                'id': 166,
                'name': "死海客户还原",
                'api': "/CrmCustomer/updateCustomerFromDeadToPoolByIds",
                'method': "POST",
                'params': "",
                'body': {"ids":38},
                'header':{'Content-Type':'application/x-www-form-urlencoded'}
            },{
                'id': 730,
                'name': "死海还原并领取",
                'api': "/CrmCustomer/receiveByIds",
                'method': "POST",
                'params': "",
                'body': {'ids': 29},
                'header':{'Content-Type':'application/x-www-form-urlencoded'}
            }
        ]
    },
    {
        'id':129,
        'name':'客户设置',
        'children':[
            {
                'id':139,
                'name':'公海管理	',
                'children':[
                    {
                        'id':142,
                        'name':"查看客户领取上限",
                        'api':"/social-api/api/crm/dictionary/reviceLimit",
                        'method':"GET",
                        'params': {},
                        'body': {}
                    },
                    {
                        'id':143,
                        'name':"编辑客户领取上限",
                        'api':"/social-api/api/crm/dictionary/edit",
                        'method':"PUT",
                        'params': {},
                        'body': {"id":"1","keyName":"client_limt","value":"11111"}
                    }
                ]
            }
        ]
    },
    {
        'id':168,
        'name':'自定义字段设置	',
        'api':'/field/queryFields',
        'method':'POST',
        'params':{},
        'body':{}
    },
]

business_data = [
    {
        'id':195,
        'name':'客户总量分析',
        'children':[
            {
                'id':196,
                'name':"查看客户总量分析",
                "api":"/biCustomer/totalCustomerStats",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'},
                "headers": {'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':204,
        'name':'客户转化率分析',
        'children':[
            {
                'id':197,
                'name':"查看客户转化率分析",
                "api":"/biCustomer/totalCustomerTable",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'},
                "headers": {'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':205,
        'name':'客户绑定率分析',
        'children':[{
                'id':198,
                'name':"查看客户绑定率分析",
                "api":"/biCustomer/customerBingdingStats",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'},
                "headers": {'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':206,
        'name':'客户跟进次数分析',
        'children':[{
                'id':199,
                'name':"查看客户跟进次数分析",
                "api":"/biCustomer/customerRecordInfo",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'},
                "headers": {'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':207,
        'name':'跟进方式分析',
        'children':[{
                'id':200,
                'name':"查看跟进方式分析",
                "api":"/biCustomer/customerRecodCategoryStats",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'},
                "headers": {'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':208,
        'name':'查看客户来源分析',
        'children':[{
                'id':201,
                'name':"查看客户来源分析",
                "api":"/biRanking/portraitSource",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year','type_analyse':'source'},
                "headers":{'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':209,
        'name':'客户总量分析',
        'children':[{
                'id':202,
                'name':"查看客户级别分析",
                "api":"/biRanking/portraitLevel",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year','type_analyse':'level'},
                "headers":{'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':210,
        'name':'新增客户排行榜',
        'children':[{
                'id':203,
                'name':"查看新增客户排行榜",
                "api":"/biRanking/customerCountRanKing",
                "method":"POST",
                "params":{},
                "body":{'deptId':'0380db65f79c422a948f8b2fafd2bc0c','type':'year'},
                "headers":{'content-tyoe': 'application/x-www-form-urlencoded'}
            }
        ]
    },{
        'id':734,
        'name':'自定义报表',
        'children':[{
                'id':732,
                'name':"自定义报表",
                "api":"/davinci-api/api/v3/dashboardPortals",
                "method":"POST",
                "params":{},
                "body":{"description":"","name":"test","publish":True,"roleIds":[],"avatar":"10","projectId":1}
            }
        ]
    }
]
system_data = [
    {
        'id':15,
        'name':'部门管理',
        'children':[
            {
                'id':16,
                'name':'查看部门列表',
                'api':'/social-api/sys/sysDepart/queryTreeList?_t=1593587922',
                'method':'GET',
                'params':{},
                'body':{}
            },
            {
                'id':17,
                'name':'创建部门',
                'api':'/social-api/sys/sysDepart/add',
                'method':'POST',
                'params':{},
                'body':{"parentId":None,"departName":"test","departOrder":0,"memo":"测试"}
            },
            {
                'id':18,
                'name':'编辑部门',
                'api':'/social-api/sys/sysDepart/edit',
                'method':'PUT',
                'params':{},
                'body':{"address":None,"children":None,"createBy":"陈飞机","createTime":"2020-07-01 15:23:15","delFlag":"0","departName":"test1111","departNameAbbr":None,"departNameEn":None,"departOrder":0,"description":None,"fax":None,"id":"2f3c7d285c0942a1a77b6b89957ad19f","isLeaf":True,"key":"2f3c7d285c0942a1a77b6b89957ad19f","memo":"测试","mobile":None,"orgCategory":"1","orgCode":"A06","orgType":"1","parentId":"","status":None,"title":"test","updateBy":None,"updateTime":None,"value":"2f3c7d285c0942a1a77b6b89957ad19f"}
            },
            {
                'id':19,
                'name':'查看部门详情',
                'api':'/social-api/sys/sysDepart/queryTreeList?_t=1593588778',
                'method':'GET',
                'params':{},
                'body':{}
            },
            {
                'id':20,
                'name':'删除部门',
                'api':'/social-api/sys/sysDepart/deleteBatch?ids=2f3c7d285c0942a1a77b6b89957ad19f',
                'method':'DELETE',
                'params':{},
                'body':{"ids":"2f3c7d285c0942a1a77b6b89957ad19f"}
            }
        ]
    },
    {
        'id':21,
        'name':'部门成员管理',
        'children':[
            {
                'id':22,
                'name':'添加已有成员',
                'api':'/social-api/sys/user/editSysDepartWithUser',
                'method':'POST',
                'params':{},
                'body':{"depId":"db83e1f4548f4397814ad3a63b94a0d1","userIdList":["74"]}
            },
            {
                'id':23,
                'name':'移除成员',
                'api':'/social-api/sys/user/deleteUserInDepart?depId=db83e1f4548f4397814ad3a63b94a0d1&userId=74',
                'method':'DELETE',
                'params':{},
                'body':{"depId":"db83e1f4548f4397814ad3a63b94a0d1","userId":"74"}
            },
            {
                'id':24,
                'name':'查看部门成员列表',
                'api':'/social-api/sys/user/departUserList',
                'method':'GET',
                'params':{"_t":"1593589395","column":"createTime","order":"desc","field":"id,,,username,realname,workNo,avatar,undefined,createBy,createTime,action","pageNo":"1","pageSize":"20","depId":"af956d2bad344012812b3df72fb0b989"},
                'body': {}
            }
        ]
    },
    {
        'id':25,
        'name':'角色管理',
        'children':[
            {
                'id':26,
                'name':'查看角色列表',
                'api':'/social-api/sys/role/list',
                'method':'POST',
                'params':{},
                'body':{"column":"createTime","order":"desc","field":"id,,,roleName,number,creatorName,departmentName,createTime,action","pageNo":1,"pageSize":20}

            },{
                'id':27,
                'name':'创建角色',
                'api':'/social-api/sys/role/add',
                'method':'POST',
                'params':{},
                'body':{"roleName":"test","roleCode":"1111","departmentId":"dfb0f10157274eda9ab3e2e6dc91c9e8","description":"测试"}

            },{
                'id':28,
                'name':'编辑角色',
                'api':'/social-api/sys/role/edit',
                'method':'PUT',
                'params':{},
                'body':{"createTime":"2020-07-01 16:02:07","creatorName":"陈飞机","departmentId":"dfb0f10157274eda9ab3e2e6dc91c9e8","departmentName":"SM技术-测试","description":None,"id":"1278237433653157890","number":0,"roleCode":"11111","roleName":"test1111"}

            },{
                'id':29,
                'name':'删除角色',
                'api':'/social-api/sys/role/delete',
                'method':'DELETE',
                'params':{"id":"1278237433653157890"},
                'body':{}

            },{
                'id':30,
                'name':'查看角色成员列表',
                'api':'/social-api/sys/role/list',
                'method':'POST',
                'params':{},
                'body':{"column":"createTime","order":"desc","field":"id,,roleCode,roleName,action","pageNo":1,"pageSize":20}

            },{
                'id':31,
                'name':'添加成员',
                'api':'/social-api/sys/user/addSysUserRole',
                'method':'POST',
                'params':{},
                'body':{"roleId":"1275681991265673217","userIdList":["74"]}

            },{
                'id':32,
                'name':'删除成员',
                'api':'/social-api/sys/user/deleteUserRole',
                'method':'DELETE',
                'params':{'roleId':1275681991265673217,'userId':74},
                'body':{}

            },{
                'id':33,
                'name':'角色权限设置',
                'api':'/social-api/sys/permission/saveRolePermissions',
                'method':'POST',
                'params':{},
                'body':{"roleId":"1260169205514780674","permissionIds":["1","2","34","801","803","804","818","213","113","123","124","125","126","127","128","129","168","6","10","11","114","115","116","117","118","119","12","120","121","1272905421392244738","1272905421425799170","1272905421455159297","1272905421488713730","1272905421513879553","1272905421551628290","1272905421580988418","1272905421606154242","1272905421631320065","1272905466141274114","1272905466170634241","1272905466199994369","1272905466225160194","1272905466250326017","1272905466267103233","1272905466288074754","1272905466309046274","1272905466334212097","13","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","15","16","165","166","167","169","17","170","171","172","173","174","175","18","19","195","196","197","198","199","20","200","201","202","203","204","205","206","207","208","209","21","210","219","22","220","221","222","223","23","24","25","26","27","28","29","3","30","31","32","33","7","701","806","807","808","809","810","811","820","821","824","9","5"],"lastPermissionIds":["1","2","34","801","803","804","818","213","113","123","124","125","126","127","128","129","168","6","10","11","114","115","116","117","118","119","12","120","121","1272905421392244738","1272905421425799170","1272905421455159297","1272905421488713730","1272905421513879553","1272905421551628290","1272905421580988418","1272905421606154242","1272905421631320065","1272905466141274114","1272905466170634241","1272905466199994369","1272905466225160194","1272905466250326017","1272905466267103233","1272905466288074754","1272905466309046274","1272905466334212097","13","130","131","132","133","134","135","136","137","138","139","140","141","142","143","144","145","146","147","15","16","165","166","167","169","17","170","171","172","173","174","175","18","19","195","196","197","198","199","20","200","201","202","203","204","205","206","207","208","209","21","210","219","22","220","221","222","223","23","24","25","26","27","28","29","3","30","31","32","33","7","701","806","807","808","809","810","811","820","821","824","9"],"objectPermissions":[{"component":"","componentName":"","id":"818","objects":[{"code":"ACCOUNT_GROUP_LIST","name":"账户组列表","lastFieldCodes":["showSensitiveInfo","channelCode","creatorName","departmentName","departmentId","createTime"],"fieldCodes":["showSensitiveInfo","channelCode","creatorName","departmentName","departmentId","createTime"],"key":"ACCOUNT_GROUP_LIST","slotTitle":"账户组列表"}],"key":"818","slotTitle":"账号组管理","permission":[],"permissionId":"818"},{"component":"","componentName":"","id":"819","objects":[{"code":"CHANNEL_LIST","name":"渠道列表","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_LIST","slotTitle":"渠道列表"}],"key":"819","slotTitle":"渠道管理","permission":[],"permissionId":"819"},{"component":None,"componentName":None,"id":"49","objects":[{"code":"IMPORT_TASK","name":"导入任务信息","lastFieldCodes":[],"fieldCodes":[],"key":"IMPORT_TASK","slotTitle":"导入任务信息"},{"code":"IMPORT_TASL_INFO","name":"导入任务明细","lastFieldCodes":[],"fieldCodes":[],"key":"IMPORT_TASL_INFO","slotTitle":"导入任务明细"}],"key":"49","slotTitle":"导入数据任务","permission":[],"permissionId":"49"},{"component":None,"componentName":None,"id":"213","objects":[{"code":"TAG_TREE_LIST","name":"标签列表","lastFieldCodes":["showSensitiveInfo"],"fieldCodes":["showSensitiveInfo"],"key":"TAG_TREE_LIST","slotTitle":"标签列表"}],"key":"213","slotTitle":"标签管理设置","permission":[],"permissionId":"213"},{"component":None,"componentName":None,"id":"113","objects":[{"code":"CRM_OBJECT_DYNAMIC.1","name":"线索信息","lastFieldCodes":["showSensitiveInfo","address","deptName","leadsName","ownerUserName","createUserName","lastFollowupTime","lastContent","createTime","nextTime","telephone","mobile","线索来源","客户级别","remark","人员","dept_id","附件","source_dept_id"],"fieldCodes":["showSensitiveInfo","address","deptName","leadsName","ownerUserName","createUserName","lastFollowupTime","lastContent","createTime","nextTime","telephone","mobile","线索来源","客户级别","remark","人员","dept_id","附件","source_dept_id"],"key":"CRM_OBJECT_DYNAMIC.1","slotTitle":"线索信息"},{"code":"CRM_OBJECT_DYNAMIC.2","name":"客户信息","lastFieldCodes":["showSensitiveInfo","address","deptName","customerName","ownerUserName","createUserName","lastFollowupTime","lastContent","createTime","nextTime","telephone","mobile","memberId","memberName","realName","客户来源","客户级别","remark","人员","dept_id","source_dept_id","字段"],"fieldCodes":["showSensitiveInfo","address","deptName","customerName","ownerUserName","createUserName","lastFollowupTime","lastContent","createTime","nextTime","telephone","mobile","memberId","memberName","realName","客户来源","客户级别","remark","人员","dept_id","source_dept_id","字段"],"key":"CRM_OBJECT_DYNAMIC.2","slotTitle":"客户信息"}],"key":"113","slotTitle":"客户管理","permission":[],"permissionId":"113"},{"component":"channel_table","componentName":"1272899620246183937","id":"1272899620346847234","objects":[{"code":"CHANNEL_TABLE_1272899620246183937","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1272899620246183937","slotTitle":"账号组"}],"key":"1272899620346847234","slotTitle":"测试","permission":[],"permissionId":"1272899620346847234"},{"component":"channel_table","componentName":"1272899911280549890","id":"1272899911309910018","objects":[{"code":"CHANNEL_TABLE_1272899911280549890","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1272899911280549890","slotTitle":"客户"}],"key":"1272899911309910018","slotTitle":"测试渠道","permission":[],"permissionId":"1272899911309910018"},{"component":"channel_table","componentName":"1272905421329330178","id":"1272905421392244738","objects":[{"code":"CHANNEL_TABLE_1272905421329330178","name":"账号组","lastFieldCodes":["showSensitiveInfo","id","applicant_company","applicant","approver_company","examination","registrant","account_type","account","password","binding_phone","account_company","account_owner"],"fieldCodes":["showSensitiveInfo","id","applicant_company","applicant","approver_company","examination","registrant","account_type","account","password","binding_phone","account_company","account_owner"],"key":"CHANNEL_TABLE_1272905421329330178","slotTitle":"账号组"}],"key":"1272905421392244738","slotTitle":"yrty","permission":[],"permissionId":"1272905421392244738"},{"component":"channel_table","componentName":"1272905466111913986","id":"1272905466141274114","objects":[{"code":"CHANNEL_TABLE_1272905466111913986","name":"账号组","lastFieldCodes":["showSensitiveInfo","id","applicant_company","applicant","approver_company","examination","registrant","account_type","account","password","binding_phone","account_company","account_owner"],"fieldCodes":["showSensitiveInfo","id","applicant_company","applicant","approver_company","examination","registrant","account_type","account","password","binding_phone","account_company","account_owner"],"key":"CHANNEL_TABLE_1272905466111913986","slotTitle":"账号组"}],"key":"1272905466141274114","slotTitle":"ryrtyrty","permission":[],"permissionId":"1272905466141274114"},{"component":"channel_table","componentName":"1272905514883280898","id":"1272905514908446721","objects":[{"code":"CHANNEL_TABLE_1272905514883280898","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1272905514883280898","slotTitle":"账号组"}],"key":"1272905514908446721","slotTitle":"rturtu","permission":[],"permissionId":"1272905514908446721"},{"component":"channel_table","componentName":"1272907761931317250","id":"1272907761952288770","objects":[{"code":"CHANNEL_TABLE_1272907761931317250","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1272907761931317250","slotTitle":"账号组"}],"key":"1272907761952288770","slotTitle":"GFDGFDG","permission":[],"permissionId":"1272907761952288770"},{"component":"channel_table","componentName":"1272911063536431105","id":"1272911063565791234","objects":[{"code":"CHANNEL_TABLE_1272911063536431105","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1272911063536431105","slotTitle":"客户"}],"key":"1272911063565791234","slotTitle":"SAHDS","permission":[],"permissionId":"1272911063565791234"},{"component":"channel_table","componentName":"1273095058131836929","id":"1273095058203140097","objects":[{"code":"CHANNEL_TABLE_1273095058131836929","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273095058131836929","slotTitle":"账号组"}],"key":"1273095058203140097","slotTitle":"验收测试","permission":[],"permissionId":"1273095058203140097"},{"component":"channel_table","componentName":"1273099515120902146","id":"1273099515146067970","objects":[{"code":"CHANNEL_TABLE_1273099515120902146","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273099515120902146","slotTitle":"账号组"}],"key":"1273099515146067970","slotTitle":"34234234356657567678665645634634663636346343463","permission":[],"permissionId":"1273099515146067970"},{"component":"channel_table","componentName":"1273136992124723202","id":"1273136992154083329","objects":[{"code":"CHANNEL_TABLE_1273136992124723202","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273136992124723202","slotTitle":"客户"}],"key":"1273136992154083329","slotTitle":"ertret","permission":[],"permissionId":"1273136992154083329"},{"component":"channel_table","componentName":"1273151241161072641","id":"1273151241190432769","objects":[{"code":"CHANNEL_TABLE_1273151241161072641","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273151241161072641","slotTitle":"账号组"}],"key":"1273151241190432769","slotTitle":"才拿到了","permission":[],"permissionId":"1273151241190432769"},{"component":"channel_table","componentName":"1273187986082684930","id":"1273187986107850753","objects":[{"code":"CHANNEL_TABLE_1273187986082684930","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273187986082684930","slotTitle":"客户"}],"key":"1273187986107850753","slotTitle":"test123","permission":[],"permissionId":"1273187986107850753"},{"component":"channel_table","componentName":"1273825050318921729","id":"1273825050348281858","objects":[{"code":"CHANNEL_TABLE_1273825050318921729","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273825050318921729","slotTitle":"客户"}],"key":"1273825050348281858","slotTitle":"ttest1","permission":[],"permissionId":"1273825050348281858"},{"component":"channel_table","componentName":"1273826184416780290","id":"1273826184446140417","objects":[{"code":"CHANNEL_TABLE_1273826184416780290","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273826184416780290","slotTitle":"账号组"}],"key":"1273826184446140417","slotTitle":"555","permission":[],"permissionId":"1273826184446140417"},{"component":"channel_table","componentName":"1273918310894854146","id":"1273918310961963009","objects":[{"code":"CHANNEL_TABLE_1273918310894854146","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273918310894854146","slotTitle":"账号组"}],"key":"1273918310961963009","slotTitle":"测试2","permission":[],"permissionId":"1273918310961963009"},{"component":"channel_table","componentName":"1273918904531476481","id":"1273918904556642305","objects":[{"code":"CHANNEL_TABLE_1273918904531476481","name":"客户","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1273918904531476481","slotTitle":"客户"}],"key":"1273918904556642305","slotTitle":"测试11","permission":[],"permissionId":"1273918904556642305"},{"component":"channel_table","componentName":"1274235680750362626","id":"1274235680775528449","objects":[{"code":"CHANNEL_TABLE_1274235680750362626","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1274235680750362626","slotTitle":"账号组"}],"key":"1274235680775528449","slotTitle":"sadsa","permission":[],"permissionId":"1274235680775528449"},{"component":"channel_table","componentName":"1277423261168230401","id":"1277423261226950657","objects":[{"code":"CHANNEL_TABLE_1277423261168230401","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1277423261168230401","slotTitle":"账号组"}],"key":"1277423261226950657","slotTitle":"测试组","permission":[],"permissionId":"1277423261226950657"},{"component":"channel_table","componentName":"1277424729468231681","id":"1277424729489203201","objects":[{"code":"CHANNEL_TABLE_1277424729468231681","name":"账号组","lastFieldCodes":[],"fieldCodes":[],"key":"CHANNEL_TABLE_1277424729468231681","slotTitle":"账号组"}],"key":"1277424729489203201","slotTitle":"测试权限","permission":[],"permissionId":"1277424729489203201"},{"component":None,"componentName":None,"id":"15","objects":[{"code":"DEPARTMENT","name":"部门","lastFieldCodes":["showSensitiveInfo","title","departName","description"],"fieldCodes":["showSensitiveInfo","title","departName","description"],"key":"DEPARTMENT","slotTitle":"部门"}],"key":"15","slotTitle":"部门管理","permission":[],"permissionId":"15"},{"component":None,"componentName":None,"id":"214","objects":[{"code":"PRODUCT_CONFIG_LIST","name":"产品列表","lastFieldCodes":[],"fieldCodes":[],"key":"PRODUCT_CONFIG_LIST","slotTitle":"产品列表"}],"key":"214","slotTitle":"产品设置","permission":[],"permissionId":"214"},{"component":None,"componentName":None,"id":"25","objects":[{"code":"ROLE","name":"角色","lastFieldCodes":["showSensitiveInfo","roleName","roleCode","departmentId","description","createBy","createTime"],"fieldCodes":["showSensitiveInfo","roleName","roleCode","departmentId","description","createBy","createTime"],"key":"ROLE","slotTitle":"角色"},{"code":"ROLE_LIST","name":"角色列表","lastFieldCodes":["showSensitiveInfo","roleName","number","creatorName","createTime"],"fieldCodes":["showSensitiveInfo","roleName","number","creatorName","createTime"],"key":"ROLE_LIST","slotTitle":"角色列表"}],"key":"25","slotTitle":"角色管理","permission":[],"permissionId":"25"},{"component":None,"componentName":None,"id":"7","objects":[{"code":"MEMBER","name":"成员","lastFieldCodes":["showSensitiveInfo","username","realname","avatar","email","phone","status"],"fieldCodes":["showSensitiveInfo","username","realname","avatar","email","phone","status"],"key":"MEMBER","slotTitle":"成员"},{"code":"MEMBER_LIST","name":"成员列表","lastFieldCodes":["showSensitiveInfo","username","realname","avatar","workNo","status","departIds","roleIds","outWeiboIds","creatorName","createTime"],"fieldCodes":["showSensitiveInfo","username","realname","avatar","workNo","status","departIds","roleIds","outWeiboIds","creatorName","createTime"],"key":"MEMBER_LIST","slotTitle":"成员列表"}],"key":"7","slotTitle":"成员管理","permission":[],"permissionId":"7"},{"component":"","componentName":"","id":"727","objects":[{"code":"OPERATION_LOG_LIST","name":"后台日志","lastFieldCodes":[],"fieldCodes":[],"key":"OPERATION_LOG_LIST","slotTitle":"后台日志"}],"key":"727","slotTitle":"操作日志","permission":[],"permissionId":"727"}]}
            }
        ]
    },
    {
        'id':7,
        'name':'成员管理',
        'children':[
            {
                "id":10,
                'name':'编辑成员',
                'api':'/social-api/sys/user/edit',
                'method':'PUT',
                'params':{},
                'body':{"avatar":None,"createTime":"2020-07-01 15:28:56","creator":"72","creatorName":"赵子龙","departIds":None,"email":None,"id":"75","outWeiboIds":"[\"\"]","phone":"","realname":"接口测试","roleIds":[{"id":"1275678397007192065","name":"角色1"}],"sex":None,"status":1,"username":"apitest","workNo":"1234568989","birthday":"","selectedroles":"1275678397007192065","selecteddeparts":""}
            },
            {
                "id":11,
                "name":"查看成员详情",
                'api':'/social-api/sys/role/queryall',
                'method':'GET',
                'params':{'_t':'1593592739'},
                'data':{}
            },
            {
                "id":12,
                "name":'删除成员',
                'api':'/social-api/sys/user/delete',
                'method':'DELETE',
                'params':{"id":"9999"},
                'data':{}
            },{
                "id":13,
                "name":'重置成员密码',
                'api':'/social-api/sys/user/resetPassword',
                'method':'PUT',
                'params':{'id':76},
                'data':{}
            },{
                "id":8,
                "name":'创建成员',
                'api':'/social-api/sys/user/list',
                'method':'GET',
                'params':{'_t':1593593110,'column':'createTime','order':'desc','field':'id,,,realname,workNo,avatar,undefined,undefined,undefined,creatorName,createTime,action','pageNo':'1','pageSize':'20'},
                'data':{}
            },{
                "id":9,
                "name":'创建成员',
                'api':'/social-api/sys/user/add',
                'method':'POST',
                'params':{},
                'data':{"username":"test222","status":0,"password":"Ss123456","confirmpassword":"sS123456","realname":"SSSSSSS","workNo":"1111","outWeiboIds":"[]","birthday":"","selectedroles":"","selecteddeparts":""}
            },
        ]
    },
    {
        'id':727,
        'name':'操作日志',
        'children':[
            {
                'id':728,
                'name':'操作日志高级查询',
                'api':'/social-api/api/crm/operLog/list/selection',
                'method':'POST',
                'params':{},
                'body':{"pageNo":1,"pageSize":20,"expression":[]}
            }
        ]
    }
]

list_test_1 = [
    {
        'id': 1,
        'name': '社交大数据平台',
        'children': [
            {
                'id': 34,
                'name': '基础数据',
                'children': base_data
            },
            {
                'id':6,
                'name':'系统设置',
                'children':system_data
            }
        ]
    }
]

list_test_2 = [
    {
        'id': 1,
        'name': '社交大数据平台',
        'children': [
            {
                'id':113,
                'name':'客户管理',
                'children':customer_data
            },
            {
                "id":194,
                'name':'商业智能',
                'children':business_data
            },
        ]
    }
]

if __name__ == '__main__':
    import requests
    print(requests.post(url='https://bd2.bd888.online/biCustomer/totalCustomerTable',headers={'Admin-Token':'d6a54dd39f334172b351b98b502cb6d2','content-tyoe':'application/x-www-form-urlencoded'},data={'deptId':'0380db65f79c422a948f8b2fafd2bc0c','userId':'','type':'year'}).content.decode('utf-8'))