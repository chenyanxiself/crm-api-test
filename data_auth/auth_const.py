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
        }
]