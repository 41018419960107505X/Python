var express = require('express');
var router = express.Router();
var mongodb=require('mongodb').MongoClient;
var db_str="mongodb://localhost:27017/zhengzhou"
/* GET users listing. */
router.get('/', function(req, res, next) {
res.send('respond with a resource');
});

//about
router.post('/about',(req,res)=>{
	
})
//post
router.post('/post',(req,res)=>{
	
})

//注册
router.post('/register',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('form',(err,coll)=>{
			coll.find({name:req.body.name}).toArray((err,data)=>{
				if(data.length>0){
					res.send('1')
				}else{
					coll.save(req.body,()=>{
						res.send('2')
					})
				}
				database.close()	
			})
		})
	})
})

//登陆
router.post('/login',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('form',(err,coll)=>{
			coll.find(req.body).toArray((err,data)=>{
				if(data.length>0){
					//把登陆用户名存储在session的name值上
					req.session.name=data[0].name
					res.send('1')
				}else{
					res.send('2')
				}
				database.close()
			})
		})
	})
})
//留言
router.post('/liuyan',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('liuyan',(err,coll)=>{
			coll.save(req.body,()=>{
				res.send('1')
				database.close()
			})
		})
	})
})
//写文章
router.post('/main',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('wenzhang',(err,coll)=>{
			coll.save(req.body,()=>{
				res.send('1')
				database.close()
			})
		})
	})
})
module.exports = router;
