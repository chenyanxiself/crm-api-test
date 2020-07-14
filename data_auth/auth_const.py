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
                                'objects':'result.data.records'
                            }]
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
                                'objects':'result.records'
                            }],
                        }
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
                                         "pageSize": 20},
                                'objects':'result.data.records'
                            }]
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
                                         "pageNo": 1, "pageSize": 20},
                                'objects':'result.records'
                            }]
                    }]
            }]
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
                         "pageNo": 1, "pageSize": 20},
                'objects': 'result.records'
            }]
        },
        {
            'id' : 850,
            'name' : '业绩数据',
            'children':[
                {
                    'id':1281492187774771202,
                    'name':'电服部',
                    'children' : [
                        {
                            'id': '1281492187867045890',
                            'name': '员工数据',
                            'children': [
                                {
                                    'id': 1281492187913183233,
                                    'name': '查看列表数据',
                                    'api': '/social-api/api/channel/channelTableProperty/performanceDatalist',
                                    'method': 'POST',
                                    'params': {},
                                    'body': {"tableId": "1281492187724439553", "column": "createTime", "order": "desc",
                                             "field": "id,", "pageNo": 1, "pageSize": 20},
                                    'objects':'result.data.records'
                                },
                            ]
                        }
                ]
                },
                {
                'id':1281492211007021058,
                'name':'代理部',
                'children':[
                    {
                        'id':1281492211095101442,
                        'name':'员工数据',
                        'children':[
                            {
                                'id': 1281492211132850177,
                                'name': '查看列表数据',
                                'api': '/social-api/api/channel/channelTableProperty/performanceDatalist',
                                'method': 'POST',
                                'params': {},
                                'body': {"tableId":"1281492210956689410","column":"createTime","order":"desc","field":"id,","pageNo":1,"pageSize":20},
                                'objects': 'result.data.records'
                            }],
                    }
            ]

            },
                {
                'id':1281492236445474817,
                'name':'市场部',
                'children':[
                    {
                        'id':1281492236541943809,
                        'name':'员工数据',
                        'children':[
                            {
                                'id': 1281492236579692545,
                                'name': '查看列表数据',
                                'api': '/social-api/api/channel/channelTableProperty/performanceDatalist',
                                'method': 'POST',
                                'params': {},
                                'body': {"tableId":"1281492236403531778","column":"createTime","order":"desc","field":"id,","pageNo":1,"pageSize":20},
                                'objects': 'result.data.records'
                            }
                        ]
                    }
                ]
            }
        ]
    },
    # {
    #     'id':1281492187825102849,
    #     'name':'电服部',
    #     'children':[
    #         {
    #             'id':1281492188265504769,
    #             'name':'查看折线图与柱状图分析报表',
    #             'api':'/social-api/api/kpi/analyseStat/fieldsStatistics',
    #             'method':'POST',
    #             'params':{},
    #             'body':{"departIds":["06ea1bcd35da481086c330410d4921f5","af956d2bad344012812b3df72fb0b989"],"userIds":["75","86"],"startTime":"2020-07-07","endTime":"2020-07-14","fieldIds":["1281492188529745922","1281492188567494657","1281492188609437697","1281492188642992130","1281492188680740866","1281492188718489602","1281585971426549761"],"tableId":"1281492187724439553"},
    #             'objects':'result'
    #         }
    #     ]
    # },
    # {
    #     'id':1281492211057352706,
    #     'name':'代理部',
    #     'children':[
    #         {
    #             'id':1281492211489366018,
    #             'name':'查看折线图与柱状图分析报表',
    #             'api':'/social-api/api/kpi/analyseStat/fieldsStatistics',
    #             'method':'POST',
    #             'params':{},
    #             'body':{"departIds":["24ab1f958b444379920fb3315a7a021e","af956d2bad344012812b3df72fb0b989"],"userIds":["192","86"],"startTime":"2020-07-07","endTime":"2020-07-14","fieldIds":["1281492211736829954","1281492211774578689","1281492211812327426","1281492211845881858","1281492211879436289"],"tableId":"1281492210956689410"},
    #             'objects': 'result'
    #
    #         }
    #     ]
    # },
    # {
    #     'id':1281492236483223553,
    #     'name':'市场部',
    #     'children':[
    #         {
    #             'id':1281492236961374210,
    #             'name':'查看折线图与柱状图分析报表',
    #             'api':'/social-api/api/kpi/analyseStat/fieldsStatistics',
    #             'method':'POST',
    #             'params':{},
    #             'body':{"departIds":["1266e415a61f4937b0e77c25b511e72f","af956d2bad344012812b3df72fb0b989"],"userIds":["191","86"],"startTime":"2020-07-07","endTime":"2020-07-14","fieldIds":["1281492237263364098","1281492237301112834","1281492237338861570","1281492237372416001","1281492237418553345"],"tableId":"1281492236403531778"},
    #             'objects': 'result'
    #
    #         }
    #     ]
    # }
]