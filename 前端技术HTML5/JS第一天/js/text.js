console.log("我是被外部引用的文件")
//此函数原样输出
console.log("<h1>sunck is a good man</h1>")
//此函数当成HTML标签使用
document.write("<h1>sunck is nice man</h1>")

var num;
num = "a";
//查看数据类型
console.log(typeof(num))

var num1 = 19;
var num2 = 29;
var sum  = num1 + num2 
//自动转换为字符串
console.log("sum = "  + sum.toString())

var num5 = 1e308
//超过了js所表示数字的范围
var num3 = Infinity
//表示不是数字,但是NAN这个值是数字类型的
//var num4 = NAN
//var num6 = NAN
console.log(typeof(num6))
console.log(isNAN(numm6))

//Boolean值
var a = true
var b =false
console.log(a)
console.log(b)

