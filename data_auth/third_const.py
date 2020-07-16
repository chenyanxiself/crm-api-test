third_auths = [
	{
		"permissionId": "818",
		"objects": [
			{

				"code": "ACCOUNT_GROUP_LIST",
				"name": "账户组列表",
				"api":"/social-api/api/channel/channel/queryAccountGroup",
				"method":"POST",
				"params":{},
				"body":{"channelFlag":2,"column":"createTime","order":"desc","field":"id,,channelCode,channelName,creatorName,createTime,status,departmentName,action","pageNo":1,"pageSize":20},
			    "objects":"result.records",
				"fields": [
					{
						"code": ["creatorName","departmentName"],
					}
				]
			}

		]
	},
	{
		"permissionId": "819",
		"objects": [
			{
				"code": "CHANNEL_LIST",
				"name": "渠道列表",
				"api":"/social-api/api/channel/channel/queryChannelAccount",
				"method":"POST",
				"params":{},
				"body":{"channelFlag":1,"column":"createTime","order":"desc","field":"id,,channelCode,channelName,creatorName,createTime,status,departmentName,action","pageNo":1,"pageSize":20},
				"objects":"result.records",
				"fields": [
					{
						"code": ["creatorName","departmentName"],
					},
				]
			}
		]
	},
	{
		"permissionId": "49",
		"objects": [
			{
				"code": "IMPORT_TASK",
				"name": "导入任务信息",
				"api":"/social-api/api/crm/importTask/select",
				"method":"POST",
				"params":{},
				"body":{"importObjectId":"0","channelId":"0","column":"createTime","order":"desc","field":"id,,,fileName,totalCount,undefined,undefined,finishMsg,departmentName,creatorName,tableName,createTime,action","pageNo":1,"pageSize":20},
				"objects":"result.records",
				"fields": [
					{
						"code": ["creatorName","departmentName"],
					},
				]
			},

		]
	},
	{
		"permissionId": "1281492187867045890",
		"objects": [
			{
				"code": "CHANNEL_TABLE_1281492187724439553",
				"name": "查看列表数据-客服部",
				"api": "/social-api/api/channel/channelTableProperty/performanceDatalist",
				"method": "POST",
				"params": {},
				"body": {"tableId": "1281492187724439553", "column": "createTime", "order": "desc", "field": "id,",
						 "pageNo": 1, "pageSize": 20},
				"objects": "result.data.records",
				"fields": [
					{
						"code": ["department","department_member"],
					}
				]
			}
		]
	}, {
		"permissionId": "1281492211095101442",
		"objects": [
			{
				"code": "CHANNEL_TABLE_1281492210956689410",
				"name": "查看列表数据-代理部",
				"api": "/social-api/api/channel/channelTableProperty/performanceDatalist",
				"method": "POST",
				"params": {},
				"body": {"tableId": "1281492210956689410", "column": "createTime", "order": "desc", "field": "id,",
						 "pageNo": 1, "pageSize": 20},
				"objects": "result.data.records",
				"fields": [
					{
						"code": ["department_member","department"],
						"name": "部门"
					}

				]
			}
		]
	}, {
		"permissionId": "1281492236541943809",
		"objects": [
			{
				"code": "CHANNEL_TABLE_1281492236403531778",
				"name": "查看列表数据-市场部",
				"api": "/social-api/api/channel/channelTableProperty/performanceDatalist",
				"method": "POST",
				"params": {},
				"body": {"tableId": "1281492236403531778", "column": "createTime", "order": "desc", "field": "id,",
						 "pageNo": 1, "pageSize": 20},
				"objects": "result.data.records",
				"fields": [
					{
						"code": ["department","department_member"],
					}
				]
			}
		]
	},
]