
# 客户问卷管理

## 查看问卷

method: `GET`

path: `/api/v1/questionnaire`

body: `none`

params:
- limit: 每页返回的数量
- state: 状态
    - 0: 操作
    - 1: 待复核
    - 2: 复合失败
    - 3: 复合成功
    - 4: 已发布
- start_id: 起始问卷id
- title: 标题
- create_time: 创建时间
- with_detail: 是否返回详细信息

response:

```json
{
    state: 200,
    msg: 'OK',
    data: {
        page:'',//总页数
        objs:[ //对象列表
                {
                    id: '',// id
                    title: '',// 标题
                    logo: '',// logo
                    datetime: '',// 创建时间
                    deadline: '',// 截止时间
                    catogory: '',// 类别
                    state: '',// 状态
                    quantity: '',// 总数量
                    free_count: '',// 待参与数量
                    background: '',// 背景图
                    marks: [
                        {
                            id:'',//标签id
                            name:'', //标签名称
                            description:'',//标签说明
                        }
                        ....
                    ],
                    // 如果请求了详细内容,name会把问题列表返回给客户端
                    // 问题列表
                    questions:[
                        {
                            id:'',//问题id
                            title:'',//标题
                            is_checkbox:''//是否多选
                            // 问题选项
                            items:[
                                id:'',//选项id
                                content:''//选项内容
                            ]
                        }
                        .....
                    ]
                    comments:[
                        {
                            id:'',//审核信息id
                            datatime:'YYYY-MM-DD',//审核时间
                            comment:'',//审核信息内容
                        }
                        .....
                    ]
                }
                .....
            ]
    }
}
```

## 创建问卷

method: `PUT`

path: `/api/v1/customer_questionnaire`

body:
- title: 标题
- deadline: 截止时间,格式:'YYYY-MM-DD'
- quantity: 数量

response:
```json
{
    state:200,
    msg:'OK',
    data:{
        id:''//创建的问卷id
    }
}
```

## 更新问卷

method: `POST`

path: `/api/v1/customer_questionnaire`

body:
- title: 标题
- deadline: 截止时间,格式:'YYYY-MM-DD'
- quantity: 数量
- state: 状态,可选[0,1]

response:
```json
{
    state:200,
    msg:'OK',
    data:{
        msg: '更新成功'
    }
}
```

## 删除问卷

method: `DELETE`

path: `/api/v1/customer_questionnaire`

body:
- ids: 数组,[1,2,3]包含要删除的问卷id

response:
```json
{
    state:200,
    msg:'OK',
    data:{
        deleted_ids: [2,3]//被删除的问卷id列表
    }
}
```

# 问卷下问题

## 创建

method: `PUT`

path: `/api/v1/customer_question`

body:
- questionnaire_id: 问卷id
- title: 提纲
- category: 问题类型
- index:题号
- items: 选项列表 [{"content":'选项1'},{"content":'选项2'},...]

response:

```json
{
    state:200,
    msg:'OK',
    data:{
        id:''//问题id
    }
}
```

## 更新

method: `POST`

path: `/api/v1/customer_question`

body:
- question_id: 问题id
- title: 提纲
- category: 问题类型
- index:题号
- items: 选项列表 [{"content":'选项1'},{"content":'选项2'},...]

response:

```json
{
    state:200,
    msg:'OK',
    data:{
        'msg': '更新成功'
    }
}
```
 
## 删除

method: `DELETE`

path: `/api/v1/customer_question`

body:
- ids: 问题id列表 [1,2,3]

response:

```json
{
    state:200,
    msg:'OK',
    data:{
        'deleted_ids': [2,3]//被删除的问题id列表
    }
}
```

# 问卷发布

method: `PUT`

path: `/api/v1/questionnaire_state`

body:
- questionnaire_id:问卷id

response:

```json
{
    state:200,
    msg:'OK',
    data:[
        {
            id:'',//审核信息id
            datatime:'YYYY-MM-DD',//审核时间
            comment:'',//审核信息内容
        }
    ]
}
```

