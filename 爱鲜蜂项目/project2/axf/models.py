from django.db import models


# Create your models here.

class SlideShow(models.Model):
    trackid = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=150)
    sort = models.CharField(max_length=20)

    class Meta:
        db_table = "slideshows"
        ordering = ['sort']


'''
id(商品id的值)
name            商品名
long_name       商品名+规格
productId      商品id
storeNums      库存
specifics       规格
sort            排序   
marketPrice    超市价格  
price           价格     
categoryId     分组id
childId       子组id
img             商品图片
keywords        搜索关键字
brandId        品牌id
brandName      品牌名称
safeDay        保质期长度
safeUnit       保质期单位模式
safeUnitDesc   保质期单位 
'''


class Product(models.Model):
    name = models.CharField(max_length=100)
    longName = models.CharField(max_length=150)
    productId = models.CharField(max_length=20)
    storeNums = models.CharField(max_length=20)
    specifics = models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
    marketPrice = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    categoryId = models.CharField(max_length=20)
    childId = models.CharField(max_length=20)
    img = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    brandId = models.CharField(max_length=20)
    brandName = models.CharField(max_length=100)
    safeDay = models.CharField(max_length=20)
    safeUnit = models.CharField(max_length=20)
    safeUnitDesc = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = "products"
        ordering = ["sort"]


'''
主体信息表   maindescription
categoryId    分组id
categoryName  分组名称
sort          排序
img           图片
product1      商品1pid
product2      商品2pid
product3      商品3pid
'''


class MainDescription(models.Model):
    categoryId = models.CharField(max_length=20)
    categoryName = models.CharField(max_length=40)
    sort = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    product1 = models.CharField(max_length=20)
    product2 = models.CharField(max_length=20)
    product3 = models.CharField(max_length=20)

    class Meta():
        db_table = "mainDescriptions"
        ordering = ["sort"]


# 分组
'''
分组表   categoriegroups
name            组名
categorieId     组id
sort            排序权重值
'''


class CategorieGroup(models.Model):
    name = models.CharField(max_length=20)
    categorieId = models.CharField(max_length=20)
    sort = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = "categoriegroups"
        ordering = ["sort"]


'''
子组表   childgroups
cid    子组id
sort   排序权重
name   子组名
categorie  分组外键
'''


class ChildGroup(models.Model):
    cid = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    sort = models.CharField(max_length=20)
    categorie = models.ForeignKey("CategorieGroup", on_delete=False)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = "childgroups"
        ordering = ["sort"]


'''
用户表      users
phoneNum     手机号(主键)
passwd      密码（允许为空）
tokenValue   token值
headImg      头像
integral     积分
vipLevel      会员等级
createTime       创建时间         
lastLoginTime     最后登陆时间
'''


class UserManager(models.Manager):
    def get_queryset(self):
        return super(UserManager, self).get_queryset().filter(isDelete=False)


class User(models.Model):
    objects = UserManager()
    phoneNum = models.CharField(max_length=20, primary_key=True)
    passwd = models.CharField(max_length=20, null=True, default=None)
    tokenValue = models.CharField(max_length=100)
    headImg = models.CharField(max_length=200)
    integral = models.IntegerField(default=0)
    vipLevel = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    lastLoginTime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = "users"

    def __str__(self):
        return self.phoneNum

    @classmethod
    def create(cls, phoneNum, passwd, tokenValue, headImg):
        return cls(phoneNum=phoneNum, passwd=passwd, tokenValue=tokenValue, headImg=headImg)


'''
地址表   addresses
name          姓名
sex           性别
phoneNum   手机号
postCode   邮编
address    收货地址
province   省份
city       城市
county     区县
street     街道
detailAddress 详细地址
user          所属用户(外键)
'''


class Address(models.Model):
    name = models.CharField(max_length=20)
    sex = models.BooleanField()
    phoneNum = models.CharField(max_length=20)
    postCode = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    province = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    county = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    detailAddress = models.CharField(max_length=200)
    user = models.ForeignKey("User", on_delete=False)

    class Meta():
        db_table = "addresses"

    def __str__(self):
        return self.address

    @classmethod
    def create(cls, name, sex, phoneNum, postCode, address, province, city, county, street, detailAddress, user):
        return cls(name=name, sex=sex, phoneNum=phoneNum, postCode=postCode, address=address, province=province,
                   city=city, county=county, street=street, detailAddress=detailAddress, user=user)


'''
购物车表  carts
user   用户
product  商品
num     数量
order  属于哪个订单
isCheck 是否被选中
isOrder 是否可用
'''


class CartManager(models.Manager):
    def get_queryset(self):
        return super(CartManager, self).get_queryset().filter(isOrder=True)


class Cart(models.Model):
    objects = CartManager()
    user = models.ForeignKey("User", on_delete=False)
    product = models.ForeignKey("Product", on_delete=False)
    order = models.ForeignKey("Order", on_delete=False)
    num = models.IntegerField()
    isCheck = models.BooleanField(default=True)
    isOrder = models.BooleanField(default=True)

    class Meta():
        db_table = "carts"

    @classmethod
    def create(cls, user, product, order, num):
        return cls(user=user, product=product, order=order, num=num)


'''
订单表       orders
orderId    订单号(主键)
user      用户
price      总价
address     地址
flag        状态
createTime   创建时间
lastTime    修改时间
isDelete   是否删除
'''


class OrderManager(models.Manager):
    def get_queryset(self):
        return super(OrderManager, self).get_queryset().get_queryset().filter(isDelete=False)


class Order(models.Model):
    orders1 = models.Manager()
    orders2 = OrderManager()
    orderId = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey("User", on_delete=False)
    address = models.ForeignKey("Address", on_delete=False)
    price = models.FloatField()
    flag = models.IntegerField(default=0)
    createTime = models.DateTimeField(auto_now_add=True)
    lastTime = models.DateTimeField(auto_now=True)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = "orders"

    @classmethod
    def create(cls, orderId, user, address, price):
        return cls(orderId=orderId, user=user, address=address, price=price)
