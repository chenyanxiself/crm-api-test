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
                'parms': {},
                'body': {"importObjectId": "0", "channelId": "0", "column": "createTime", "order": "desc",
                         "field": "id,,,fileName,totalCount,undefined,undefined,finishMsg,departmentName,creatorName,tableName,createTime,action",
                         "pageNo": 1, "pageSize": 20}
            },
            {
                'id': 51,
                'name': '查看导入任务明细',
                'api': '/social-api/api/crm/importTaskInfo/list',
                'method': 'POST',
                'parms': {},
                'body': {"column": "createTime", "order": "desc", "field": "id,", "pageNo": 1, "pageSize": 20,
                         "importTaskId": "1274232437353799682", "importObjectId": "1273825050318921729"}
            },
            {
                'id': 53,
                'name': '下载失败数据',
                'api': '/social-api/api/crm/importTaskInfo/export',
                'method': 'POST',
                'parms': {},
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
                'parms': {},
                'body': {}
            },
            {
                'id': 220,
                'name': '创建标签',
                'api': '/social-api/api/channel/tag/add',
                'method': 'POST',
                'parms': {},
                'body': {"name": "test", "categoryId": "1273444722643361794"}
            },
            {
                'id': 221,
                'name': '编辑标签',
                'api': '/social-api/api/channel/tag/edit',
                'method': 'PUT',
                'parms': {},
                'body': {"id":"12","name":"1","type":2,"categoryId":"1"}
            },
            {
                'id': 222,
                'name': '删除标签',
                'api': '/social-api/api/channel/tag/delete?id=1277896932286586882',
                'method': 'DELETE',
                'parms': {'id': '1277896932286586882'},
                'body': {}
            },
            {
                'id': 223,
                'name': '编辑标签分类',
                'api': '/social-api/api/channel/tagCategory/edit',
                'method': 'PUT',
                'parms': {},
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
                'parms': {},
                'body': {"name": "test"}
            },
            {
                'id': 225,
                'name': '删除标签分类',
                'api': '/social-api/api/channel/tagCategory/delete?id=1277898581335924738',
                'method': 'DELETE',
                'parms': {},
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
                'parms': {},
                'body': {"column": "createTime", "order": "desc", "field": "id,,,name,creatorName,createTime,action",
                         "pageNo": 1, "pageSize": 20}
            },
            {
                'id': 216,
                'name': '创建产品',
                'api': '/social-api/api/channel/product/add',
                'method': 'POST',
                'parms': {},
                'body': {"name": "test"}
            },
            {
                'id': 217,
                'name': '编辑产品',
                'api': '/social-api/api/channel/product/edit',
                'method': 'PUT',
                'parms': {},
                'body': {"createTime": "2020-05-01 00:01:18", "creator": "13", "creatorName": "冯十一", "delFlag": 2,
                         "id": "1255889975163518977", "name": "产品b", "status": 1}
            },
            {
                'id': 218,
                'name': '查看产品',
                'api': '/social-api/api/channel/product/delete?id=1277900893739606017',
                'method': 'DELETE',
                'parms': {'id': '1277900893739606017'},
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
                'id': 169,
                'name': '查看新增线索',
                'api': '/CrmBackLog/todayLeads',
                'method': 'POST',
                'parms': {},
                'body': {"page": 1, "limit": 15, "search": "", "type": 4, "isSub": 1, "label": 2}
            }, {
                'id': 170,
                'name': '查看新增客户',
                'api': '/CrmBackLog/todayCustomer',
                'method': 'POST',
                'parms': {},
                'body': {"page": 1, "limit": 15, "search": "", "type": 5, "isSub": 1, "label": 2}
            }, {
                'id': 171,
                'name': '查看新增跟进记录',
                'api': '/Crm/Instrument/queryRecordConunt',
                'method': 'POST',
                'parms': {},
                'body': {"page": 1, "limit": 15, "search": "", "type": 4, "isSub": 1, "label": 2}
            }, {
                'id': 172,
                'name': '查看逾期未联系客户',
                'api': '/CrmBackLog/todayCustomer',
                'method': 'POST',
                'parms': {},
                'body': {"page": 1, "limit": 15, "search": "", "type": 2, "isSub": 1, "label": 2}
            }, {
                'id': 173,
                'name': '查看逾期未联系线索',
                'api': '/CrmBackLog/todayLeads',
                'method': 'POST',
                'parms': {},
                'body': {"page": 1, "limit": 15, "search": "", "type": 2, "isSub": 1, "label": 2}
            }, {
                'id': 713,
                'name': '客户转化阶段漏斗',
                'api': '/biCustomer/convertcus',
                'method': 'POST',
                'parms': {},
                'body': {"startTime": "2020-06-30 00:00:00", "endTime": "2020-06-30 23:59:59", "creator": "73"},
                'header': {'Content-Type': 'application/x-www-form-urlencoded'}
            }, {
                'id': 714,
                'name': '新增客户跟进状态漏斗',
                'api': '/biCustomer/cusfollow',
                'method': 'POST',
                'parms': {},
                'body': {"startTime": "2020-06-30 00:00:00", "endTime": "2020-06-30 23:59:59", "creator": "73"},
                'header': {'Content-Type': 'application/x-www-form-urlencoded'}
            },
        ]
    },
    {
        'id': 124,
        'name': '待办事项',
        'children': [
            {
                'id': 130,
                'name': '今日需联系线索',
                'children': [
                    {
                        'id': 133,
                        'name': "查看今日需联系线索",
                        'api': "/CrmBackLog/todayLeads",
                        'method': "POST",
                        'parms': "",
                        'body': {"page": 1, "limit": 15, "isSub": 1, "type": 1}
                    }
                ]
            },
            {
                'id': 131,
                'name': '今日需联系客户',
                'children': [
                    {
                        'id': 134,
                        'name': '查看今日需联系客户',
                        'api': "/CrmBackLog/todayCustomer",
                        'method': "POST",
                        'parms': {},
                        'body': {"page": 1, "limit": 15, "isSub": 1, "type": 2}
                    }

                ]
            },
            {
                'id': 132,
                'name': '分配给我的线索',
                'children': [
                    {
                        'id': 135,
                        'name': '查看分配给我的线索',
                        'api': "/CrmBackLog/followLeads",
                        'method': "POST",
                        'parms': {},
                        'body': {"page": 1, "limit": 15, "isSub": 1, "type": 2}
                    }

                ]
            }, {
                'id': 136,
                'name': '我的客户',
                'children': [
                    {
                        'id': 137,
                        'name': '查看分配给我的客户',
                        'api': "/CrmBackLog/followCustomer",
                        'method': "POST",
                        'parms': {},
                        'body': {"page": 1, "limit": 15, "isSub": 1, "type": 2}
                    }

                ]
            }, {
                'id': 174,
                'name': '查看待进公海客户',
                'children': [
                    {
                        'id': 175,
                        'name': '查看待进公海客户',
                        'api': "/CrmBackLog/putInPoolRemind",
                        'method': "POST",
                        'parms': {},
                        'body': {"page": 1, "limit": 15, "isSub": 1, "type": 2}
                    }

                ]
            }
        ]
    },
    {
        'id': 125,
        'name': '线索',
        'children': [
            {
                'id': 144,
                'name': "查看线索列表",
                'api': "/CrmLeads/queryPageList",
                'method': "POST",
                'parms': "",
                'body': {"page": 2, "limit": 15, "search": "", "type": 1}
            }
        ]
    },
    {
        'id': 126,
        'name': '客户',
        'children': [
            {
                'id': 145,
                'name': "查看客户列表",
                'api': "/CrmCustomer/queryPageList",
                'method': "POST",
                'parms': "",
                'body': {"page": 1, "limit": 15, "search": "", "type": 2}
            }
        ]
    },
    {
        'id': 127,
        'name': '公海',
        'children': [
            {
                'id': 146,
                'name': "查看公海列表",
                'api': "/CrmCustomer/queryPoolPageList",
                'method': "POST",
                'parms': "",
                'body': {"page": 2, "limit": 15, "search": "", "type": 9}
            },
            {
                'id': 731,
                'name': "公海领取",
                'api': "/CrmCustomer/receiveByIds",
                'method': "POST",
                'parms': "",
                'body': {"ids": 38},
                'header': {'Content-Type': 'application/x-www-form-urlencoded'}
            }
        ]
    },
    {
        'id': 128,
        'name': '死海',
        'children': [
            {
                'id': 147,
                'name': "查看死海列表",
                'api': "/CrmCustomer/queryPoolPageList",
                'method': "POST",
                'parms': "",
                'body': {"page": 1, "limit": 15, "search": "", "type": 10}
            }, {
                'id': 166,
                'name': "死海客户还原",
                'api': "/CrmCustomer/updateCustomerFromDeadToPoolByIds",
                'method': "POST",
                'parms': "",
                'body': {"ids": 38},
                'header': {'Content-Type': 'application/x-www-form-urlencoded'}
            }, {
                'id': 730,
                'name': "死海还原并领取",
                'api': "/CrmCustomer/receiveByIds",
                'method': "POST",
                'parms': "",
                'body': {'ids': 29},
                'header': {'Content-Type': 'application/x-www-form-urlencoded'}
            }
        ]
    },
    {
        'id': 129,
        'name': '客户设置',
        'children': [
            {
                'id': 139,
                'name': '公海管理	',
                'children': [
                    {
                        'id': 142,
                        'name': "查看客户领取上限",
                        'api': "/social-api/api/crm/dictionary/reviceLimit",
                        'method': "GET",
                        'parms': {},
                        'body': {}
                    },
                    {
                        'id': 143,
                        'name': "编辑客户领取上限",
                        'api': "/social-api/api/crm/dictionary/edit",
                        'method': "PUT",
                        'parms': {},
                        'body': {"id": "1", "keyName": "client_limt", "value": "11111"}
                    }
                ]
            }
        ]
    },
    {
        'id': 168,
        'name': '自定义字段设置	',
        'api': 'field/queryFields',
        'method': 'POST',
        'parms': {},
        'body': {}
    },
]

list_test = [
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
                'id':113,
                'name':'客户管理',
                'children':customer_data
            }
        ]
    }
]
