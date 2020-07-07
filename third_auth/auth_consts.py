third_data=[
	{
		"permissionId": "818",
		"objects": [
			{
				"code": "ACCOUNT_GROUP_LIST",
				"name": "账户组列表",
				"api":"/social-api/api/channel/channel/queryAccountGroup",
				"method":"POST",
				"params":{},
				"json":{"channelFlag":2,"column":"createTime","order":"desc","field":"id,,channelCode,channelName,creatorName,createTime,status,departmentName,action","pageNo":1,"pageSize":20},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "channelCode",
						"name": "账号组编号"
					},
					{
						"code": "creatorName",
						"name": "创建人"
					},
					{
						"code": "departmentName",
						"name": "部门名称"
					},
					{
						"code": "departmentId",
						"name": "部门Id"
					},
					{
						"code": "createTime",
						"name": "创建时间"
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
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "channelCode",
						"name": "渠道编号"
					},
					{
						"code": "creatorName",
						"name": "创建人"
					},
					{
						"code": "departmentName",
						"name": "部门名称"
					},
					{
						"code": "departmentId",
						"name": "部门Id"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					}
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
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "fileName",
						"name": "导入文件名"
					},
					{
						"code": "fileUrl",
						"name": "下载文件路径"
					},
					{
						"code": "totalCount",
						"name": "导入记录数"
					},
					{
						"code": "successCount",
						"name": "成功导入数量"
					},
					{
						"code": "failCount",
						"name": "导入失败数量"
					},
					{
						"code": "waitCount",
						"name": "待导入数量"
					},
					{
						"code": "status",
						"name": "状态"
					},
					{
						"code": "createTime",
						"name": "导入时间"
					},
					{
						"code": "departmentName",
						"name": "导入部门"
					},
					{
						"code": "creatorName",
						"name": "导入人"
					},
					{
						"code": "tableName",
						"name": "导入对象表"
					},
					{
						"code": "finishMsg",
						"name": "完成信息"
					}
				]
			},
			{
				"code": "IMPORT_TASL_INFO",
				"name": "导入任务明细",
				"api":"/social-api/api/crm/importTaskInfo/list",
				"method":"POST",
				"params":{},
				"json":{"column":"createTime","order":"desc","field":"id,","pageNo":1,"pageSize":20,"importTaskId":"1277523065906978817","importObjectId":"1277521819573739521"},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "content",
						"name": "导入内容"
					},
					{
						"code": "createTime",
						"name": "导入时间"
					},
					{
						"code": "creator",
						"name": "导入人"
					},
					{
						"code": "finishMsg",
						"name": "完成信息"
					},
					{
						"code": "status",
						"name": "状态"
					}
				]
			}
		]
	},
	{
		"permissionId": "213",
		"objects": [
			{
				"code": "TAG_TREE_LIST",
				"name": "标签列表",
				"api":"/social-api/api/channel/tagCategory/tree",
				"method":"POST",
				"params":{},
				"json":{},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					}
				]
			}
		]
	},
	{
		"permissionId": "113",
		"objects": [
			{
				"code": "CRM_OBJECT_DYNAMIC.1",
				"name": "线索信息",
				"api":"/CrmLeads/queryPageList",
				"method":"POST",
				"params":{},
				"json":{"page":1,"limit":15,"search":"","type":1},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "address",
						"name": "地址"
					},
					{
						"code": "deptName",
						"name": "部门名称"
					},
					{
						"code": "leadsName",
						"name": "线索名称"
					},
					{
						"code": "ownerUserName",
						"name": "负责人"
					},
					{
						"code": "createUserName",
						"name": "创建人"
					},
					{
						"code": "lastFollowupTime",
						"name": "上次跟进时间"
					},
					{
						"code": "lastContent",
						"name": "上次跟进内容"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					},
					{
						"code": "nextTime",
						"name": "下次联系时间"
					},
					{
						"code": "telephone",
						"name": "电话"
					},
					{
						"code": "mobile",
						"name": "手机"
					},
					{
						"code": "线索来源",
						"name": "线索来源"
					},
					{
						"code": "客户级别",
						"name": "客户级别"
					},
					{
						"code": "remark",
						"name": "备注"
					},
					{
						"code": "人员",
						"name": "人员"
					},
					{
						"code": "单行文本",
						"name": "单行文本"
					},
					{
						"code": "dept_id",
						"name": "部门"
					},
					{
						"code": "附件",
						"name": "附件"
					},
					{
						"code": "日期",
						"name": "日期"
					},
					{
						"code": "日期时间",
						"name": "日期时间"
					},
					{
						"code": "货币",
						"name": "货币"
					},
					{
						"code": "数字",
						"name": "数字"
					},
					{
						"code": "多选",
						"name": "多选"
					},
					{
						"code": "下拉框",
						"name": "下拉框"
					},
					{
						"code": "source_dept_id",
						"name": "来源部门"
					},
					{
						"code": "activity_id",
						"name": "营销活动"
					}
				]
			},
			{
				"code": "CRM_OBJECT_DYNAMIC.2",
				"name": "客户信息",
				"api":"/CrmCustomer/queryPageList",
				"method":"POST",
				"params":{},
				"json":{"page":1,"limit":15,"search":"","type":2},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "address",
						"name": "地址"
					},
					{
						"code": "deptName",
						"name": "部门名称"
					},
					{
						"code": "customerName",
						"name": "客户名称"
					},
					{
						"code": "ownerUserName",
						"name": "负责人"
					},
					{
						"code": "createUserName",
						"name": "创建人"
					},
					{
						"code": "lastFollowupTime",
						"name": "上次跟进时间"
					},
					{
						"code": "lastContent",
						"name": "上次跟进内容"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					},
					{
						"code": "nextTime",
						"name": "下次联系时间"
					},
					{
						"code": "telephone",
						"name": "电话"
					},
					{
						"code": "mobile",
						"name": "手机"
					},
					{
						"code": "memberId",
						"name": "会员ID"
					},
					{
						"code": "memberName",
						"name": "会员昵称"
					},
					{
						"code": "realName",
						"name": "真实姓名"
					},
					{
						"code": "客户来源",
						"name": "客户来源"
					},
					{
						"code": "客户级别",
						"name": "客户级别"
					},
					{
						"code": "remark",
						"name": "备注"
					},
					{
						"code": "多行文本",
						"name": "多行文本"
					},
					{
						"code": "人员",
						"name": "人员"
					},
					{
						"code": "附件",
						"name": "附件"
					},
					{
						"code": "dept_id",
						"name": "部门"
					},
					{
						"code": "source_dept_id",
						"name": "来源部门"
					},
					{
						"code": "activity_id",
						"name": "营销活动"
					},
					{
						"code": "日期",
						"name": "日期"
					}
				]
			}
		]
	},
	{
		"permissionId": "15",
		"objects": [
			{
				"code": "DEPARTMENT",
				"name": "部门",
				"api":"/social-api/sys/sysDepart/queryTreeList",
				"method":"GET",
				"params":{"_t":1594090623},
				"json":{},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "title",
						"name": "树级部门名称"
					},
					{
						"code": "departName",
						"name": "部门名称"
					},
					{
						"code": "description",
						"name": "描述"
					}
				]
			}
		]
	},
	{
		"permissionId": "214",
		"objects": [
			{
				"code": "PRODUCT_CONFIG_LIST",
				"name": "产品列表",
				"api":"/social-api/api/channel/product/list",
				"method":"POST",
				"params":{},
				"json":{"column":"createTime","order":"desc","field":"id,,,name,creatorName,createTime,action","pageNo":1,"pageSize":20},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					}
				]
			}
		]
	},
	{
		"permissionId": "25",
		"objects": [
			{
				"code": "ROLE",
				"name": "角色",
				"api":"/social-api/sys/role/list",
				"method":"POST",
				"params": {},
				"json":{"departmentId":"1266e415a61f4937b0e77c25b511e72f","column":"createTime","order":"desc","field":"id,,,roleName,number,creatorName,departmentName,typeName,createTime,sort,action","pageNo":1,"pageSize":20},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "roleName",
						"name": "角色名"
					},
					{
						"code": "roleCode",
						"name": "角色编码"
					},
					{
						"code": "departmentId",
						"name": "所属部门"
					},
					{
						"code": "description",
						"name": "描述"
					},
					{
						"code": "createBy",
						"name": "创建人"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					}
				]
			},
			{
				"code": "ROLE_LIST",
				"name": "角色列表",
				"api":"/social-api/sys/sysDepart/queryTreeWithCountList",
				"method":"GET",
				"params":{"_t":"1594090940"},
				"json":{},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "roleName",
						"name": "角色名称"
					},
					{
						"code": "number",
						"name": "人数"
					},
					{
						"code": "creatorName",
						"name": "创建人"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					}
				]
			}
		]
	},
	{
		"permissionId": "7",
		"objects": [
			{
				"code": "MEMBER",
				"name": "成员",
				"api":"/social-api/sys/user/list",
				"method":"GET",
				"params":{},
				"json":{"_t":1594090986,"column":"createTime","order":"desc","field":"id,,,realname,workNo,avatar,undefined,undefined,undefined,creatorName,createTime,action","pageNo":1,"pageSize":20},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "username",
						"name": "用户名"
					},
					{
						"code": "realname",
						"name": "真实姓名"
					},
					{
						"code": "avatar",
						"name": "头像"
					},
					{
						"code": "email",
						"name": "邮箱"
					},
					{
						"code": "phone",
						"name": "电话"
					},
					{
						"code": "status",
						"name": "状态"
					}
				]
			},
			{
				"code": "MEMBER_LIST",
				"name": "成员列表",
				"api":"/social-api/sys/user/list",
				"method":"GET",
				"params":{},
				"json":{"_t":1594090986,"column":"createTime","order":"desc","field":"id,,,realname,workNo,avatar,undefined,undefined,undefined,creatorName,createTime,action","pageNo":1,"pageSize":20},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "username",
						"name": "用户名"
					},
					{
						"code": "realname",
						"name": "真实姓名"
					},
					{
						"code": "avatar",
						"name": "头像"
					},
					{
						"code": "workNo",
						"name": "工号"
					},
					{
						"code": "status",
						"name": "状态"
					},
					{
						"code": "departIds",
						"name": "部门"
					},
					{
						"code": "roleIds",
						"name": "角色"
					},
					{
						"code": "outWeiboIds",
						"name": "外部微博id"
					},
					{
						"code": "creatorName",
						"name": "创建人"
					},
					{
						"code": "createTime",
						"name": "创建时间"
					}
				]
			}
		]
	},
	{
		"permissionId": "727",
		"objects": [
			{
				"code": "OPERATION_LOG_LIST",
				"name": "后台日志",
				"api":"/social-api/api/crm/operLog/list/selection",
				"method":"POST",
				"params":{},
				"json":{"pageNo":1,"pageSize":20,"expression":[]},
				"fields": [
					{
						"code": "showSensitiveInfo",
						"name": "显示敏感信息"
					},
					{
						"code": "createName",
						"name": "创建人"
					},
					{
						"code": "content",
						"name": "操作内容"
					}
				]
			}
		]
	}
]