var express = require('express');
var router = express.Router();
var ObjectId=require('mongodb').ObjectId;
var mongodb=require('mongodb').MongoClient;
var db_str="mongodb://localhost:27017/zhengzhou"
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('main', {name:req.session.name});
});
//主页
router.get('/main',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('wenzhang',(err,coll)=>{
			coll.find({}).toArray((err,data)=>{
				res.render('main',{data:data})
				database.close()
			})
		})
	})	
})
//about
router.get('/about',(req,res)=>{
	res.render('about',{})
})
//post
router.get('/post',(req,res)=>{
	res.render('post',{})
})
//注册
router.get('/register',(req,res)=>{
	res.render('register',{})
})

//登陆
router.get('/login',(req,res)=>{
	res.render('login',{})
})
//留言
router.get('/liuyan',(req,res)=>{
	mongodb.connect(db_str,(err,database)=>{
		database.collection('liuyan',(err,coll)=>{
			coll.find({}).sort({_id:-1}).toArray((err,data)=>{
				res.render('liuyan',{data:data})
				database.close()
			})
		})
	})	
})

//留言详情
router.get('/message',(req,res)=>{
	var id=ObjectId(req.query.id)
	mongodb.connect(db_str,(err,database)=>{
		database.collection('liuyan',(err,coll)=>{
			coll.find({_id:id}).toArray((err,data)=>{
				res.render('message',{result:data[0]})
				database.close()
			})
		})
	})	
})

module.exports = router;
