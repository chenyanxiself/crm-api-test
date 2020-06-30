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
                                'id': 814,
                                'name': '删除汇总数据',
                                'api': '/social-api/api/channel/channelTableValue/accountGroupCollectDelete/123456721',
                                'method': 'DELETE',
                                'params': {},
                                'body': {},
                            },
                            {
                                'id': 809,
                                'name': '查看报表统计',
                                'api': 'social-api/api/channel/statistical/accountGroup/overview?_t=1593503484&channelFlag=2',
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
                                'api': '/social-api/api/channel/channelTableValue/delete/1273096166979985409',
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
                                'api': '/social-api/api/channel/channel/queryChannelAccount',
                                'params': {},
                                'body': {"channelFlag": 1, "column": "createTime", "order": "desc",
                                         "field": "id,,channelCode,channelName,creatorName,createTime,status,departmentName,action",
                                         "pageNo": 1, "pageSize": 20}
                            },
                            {
                                'id': 817,
                                'name': '编辑',
                                'api': '/social-api/api/channel/channel/editAccountGroup',
                                'params': {},
                                'body': {"channelFlag": 1, "name": "测试", "code": "CS",
                                         "departmentId": ["c82826768f644be8be737c2bdd2952aa"],
                                         "id": "1277886208147513345"}
                            },
                            {
                                'id': 822,
                                'name': '启用',
                                'api': '/social-api/api/channel/channel/enabledChannel',
                                'params': {},
                                'body': {"id": "1277886208147513345"}
                            },
                            {
                                'id': 823,
                                'name': '禁用',
                                'api': '/social-api/api/channel/channel/disabledChannel',
                                'params': {},
                                'body': {"id": "1277886208147513345"}
                            },
                            {
                                'id': 825,
                                'name': '新建',
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
                'api': '/social-api/api/channel/tagCategory/edit',
                'method': 'PUT',
                'parms': {},
                'body': {"id": "1273444722643361794", "name": "test", "children": [
                    {"id": "1274222560149561346", "name": "kevin", "type": 2, "categoryId": "1273444722643361794"},
                    {"id": "1277438167582040065", "name": "1", "type": 2, "categoryId": "1273444722643361794"},
                    {"id": "1277896932286586882", "name": "test", "type": 2, "categoryId": "1273444722643361794"}],
                         "type": 1}
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
        ]
    }
]
