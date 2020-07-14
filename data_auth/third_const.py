third_auths = [{
		"permissionId": "818",
		"objects": [
			{

				"code": "ACCOUNT_GROUP_LIST",
				"name": "账户组列表",
				"api":"/social-api/api/channel/channel/queryAccountGroup",
				"method":"POST",
				"params":{},
				"json":{"channelFlag":2,"column":"createTime","order":"desc","field":"id,,channelCode,channelName,creatorName,createTime,status,departmentName,action","pageNo":1,"pageSize":20},
			    "regExp_response":"result.records",
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
				"json":{"channelFlag":1,"column":"createTime","order":"desc","field":"id,,channelCode,channelName,creatorName,createTime,status,departmentName,action","pageNo":1,"pageSize":20},
				"regExp_response":"result.records",
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
				"json":{"importObjectId":"0","channelId":"0","column":"createTime","order":"desc","field":"id,,,fileName,totalCount,undefined,undefined,finishMsg,departmentName,creatorName,tableName,createTime,action","pageNo":1,"pageSize":20},
				"regExp_response":"result.records",
				"fields": [
					{
						"code": ["creatorName","departmentName"],
					},
				]
			},

		]
	}
]