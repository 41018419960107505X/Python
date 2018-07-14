# 问卷审核

管理员只能提交审核信息,不能查看提交的审核历史

## 提交审核

method: `PUT`

path: `/api/v1/questionnaire_comment`

body:
- questionnaire_id:问卷id
- is_agree:是否通过
- comment:审核信息

response:

```json
{
    state:200,
    msg:'OK',
    data:{
        'msg': '提交审核内容成功'
    }
}
```

## 获取待审核问卷

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
```