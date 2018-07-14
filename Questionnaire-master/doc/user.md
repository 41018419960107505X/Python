# 问卷参与信息

## 获取问卷参与信息

method: `GET`

path: `/api/v1/questionnaire_join`

body:

- limit:每页数量
- start_id:起始id
- is_done:是否已经完成

```json
{
    state:200,
    msg:'OK',
    data:[
        {
            id:'',//信息id
            create_time:'',//创建时间
            is_done:'',//状态
            questionnaire:{
                id:'',//问卷id
                title:''//问卷笔记
            }
        }
        .....
    ]
}
```

## 参与问卷

method: `PUT`

path: `/api/v1/questionnaire_join`

body:
- questionnaire_id:问卷id

```json
{
    state:200,
    msg:'OK',
    data:{
        id:''//新建的id
    }
}
```

## 退出问卷参与

method: `DELETE`

path: `/api/v1/questionnaire_join`

body:
- ids: 参与信息id列表

```json
{
    state:200,
    msg:'OK',
    data:{
        'deleted_ids': []//被删除的id列表
    }
}
```

# 问卷答案

## 获取问卷答案

method: `GET`

path: `/api/v1/questionnaire_answer`

body: `none`

params:
- questionnaire_id:问卷id

```json
{
    state:200,
    msg:'OK',
    data:[
        {
            question_id:'',//问题id
            title:'',//提纲
            items:[
                {
                    id:'',//选项id
                    content:'',//选项内容
                }
                ......
            ]
        }
        .....
    ]
}
```


## 提交问卷答案

method: `PUT`

path: `/api/v1/questionnaire_answer`

body:
- questionnaire_id:问卷id
- questions:问题及选项
```
[
    {
        "question_id":'',问题id
        "items":[1,2,3],选择的问题
    }
    .....
]
```
- is_done:是否完成


response:

```json
{
    state:200,
    msg:'OK',
    data:{
        'msg': "提交成功"
    }
}
```


## 更新问卷答案

method: `POST`

path: `/api/v1/questionnaire_answer`

body:
- questionnaire_id:问卷id
- questions:问题及选项
```
[
    {
        "question_id":'',问题id
        "items":[1,2,3],选择的问题
    }
    .....
]
```
- is_done:是否完成


response:

```json
{
    state:200,
    msg:'OK',
    data:{
        'msg': "提交成功"
    }
}
```

# 获取问卷列表

method: `GET`

path: `/api/v1/questionnaire`

body: none

params:
- limit:每页数量
- with_detail:是否查看详细信息
- start_id:起始id
- page:页面

response:

```json
{
    state: 200,
    msg: 'OK',
    data: [
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
        }
        .....
    ]
}
```