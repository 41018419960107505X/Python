from django.shortcuts import render, redirect

from axf.models import SlideShow, MainDescription, Product, CategorieGroup, ChildGroup, User, Address, Cart, Order

# Create your views here.
# from rest_framework.response import Response
from django.http import JsonResponse


# from rest_framework import status
# from axf.serializers import SlideShowSerializer, MainDescriptionSerializer
# #轮播接口
# def SlideShows(request):
#     if request.method == "GET":
#         slideList = SlideShow.objects.all()
#         serializer = SlideShowSerializer(slideList, many=True)
#         return JsonResponse(serializer.data, safe=False)
#   #五个模块接口
# def MainDescriptions(request):
#     if request.method == "GET":
#         mainList = MainDescription.objects.all()
#         serializer = MainDescriptionSerializer(mainList, many=True)
#         return JsonResponse(serializer.data, safe=False)
# 五个模块中展示商品的接口
# def Products(request, pid):
#
#


def home(request):
    # 获取轮播图数据
    slideList = SlideShow.objects.all()

    # 获取5大模块数据
    mainList = MainDescription.objects.all()
    for item in mainList:
        products = Product.objects.filter(categoryId=item.categoryId)
        item.product1 = products.get(productId=item.product1)
        item.product2 = products.get(productId=item.product2)
        item.product3 = products.get(productId=item.product3)
    return render(request, "home/home.html", {"slideList": slideList, "mainList": mainList})


# 闪送超市
def market(request, gid, cid, sid):
    # 左侧分组数据
    leftCategorieList = CategorieGroup.objects.all()

    # 获取分组商品的信息
    products = Product.objects.filter(categoryId=gid)
    # 获取子类数据
    if cid != "0":
        products = products.filter(childId=cid)
    # 排序
    if sid == "1":
        # products = products.order_by()
        pass
    elif sid == "2":
        products = products.order_by("price")
    elif sid == "3":
        products = products.order_by("-price")

    # 获取子组信息
    childs = ChildGroup.objects.filter(categorie__categorieId=gid)
    return render(request, "market/market.html",
                  {"leftCategorieList": leftCategorieList, "products": products, "childs": childs, "gid": gid,
                   "cid": cid})


# 购物车
def cart(request):
    print('==============1')
    # 判断用户是否登陆
    tokenValue = request.COOKIES.get("token")
    print('==============2')
    if not tokenValue:
        return redirect('/login/')
    try:
        # 找到用户
        user = User.objects.get(tokenValue=tokenValue)
    except User.DoesNotExist as e:
        return redirect('/login/')
    carts = Cart.objects.filter(user__tokenValue=tokenValue)
    print('==============3')
    return render(request, "cart/cart.html", {"carts": carts})


def changecart(request, flag):
    num = 1
    if flag == "1":
        num = -1
    tokenValue = request.COOKIES.get("token")
    if not tokenValue:
        return JsonResponse({"error": 1})
    try:
        # 找到用户
        user = User.objects.get(tokenValue=tokenValue)
    except User.DoesNotExist as e:
        return JsonResponse({"error": 2})

    gid = request.POST.get("gid")
    cid = request.POST.get("cid")
    pid = request.POST.get("pid")
    # 找到商品
    product = Product.objects.filter(categoryId=gid, childId=cid).get(productId=pid)
    # 找到该商品的购物车数据
    try:
        cart = Cart.objects.filter(user__tokenValue=tokenValue).filter(product__categoryId=gid).filter(
            product__childId=cid).get(product__productId=pid)
        # 添加商品时，如果商品库存为0，就不在添加，数据（num）返回
        if flag == "2":
            if product.storeNums == "0":
                return JsonResponse({"error": 0, "num": cart.num})
        # 买过商品，把购物车数据加上
        cart.num = cart.num + num
        # 减该商品库存
        product.storeNums = str(int(product.storeNums) - num)
        product.save()
        # 当商品数量为0时，删除购物车数据。不为0保存数据
        if cart.num == 0:
            cart.delete()
        else:
            cart.save()
    except Cart.DoesNotExist as e:
        # 没有该商品购物车数据，点击减商品时，不会有变化。
        if flag == "1":
            return JsonResponse({"error": 0, "num": 0})
        # 数据不存在说明没有买过该商品，创建数据添加到购物车。
        # 找到一个可用的订单flag为0的
        try:
            order = Order.orders2.filter(user__tokenValue=tokenValue).get(flag=0)
        except Order.DoesNotExist as e:
            # 没有可用订单，创建订单
            orderId = str(uuid.uuid4())
            address = Address.objects.get(pk=1)
            order = Order.create(orderId, user, address, 0)
            order.save()
        # 没有购买过该商品，创建购物车数据
        cart = Cart.create(user, product, order, 1)
        cart.save()
        # 减该商品库存
        product.storeNums = str(int(product.storeNums) - num)
        product.save()
        # 把数据返回
    return JsonResponse({"error": 0, "num": cart.num})


# 修改购物车是否被选中
def changecart1(request):
    cartid = request.POST.get("cartid")
    cart = Cart.objects.get(pk=cartid)
    cart.isCheck = not cart.isCheck
    cart.save()
    return JsonResponse({"error": 0, "flag": cart.isCheck})


# 下单
def Orders(request):
    tokenValue = request.COOKIES.get("token")
    # 找到可用订单,状态给成不可用
    order = Order.orders2.filter(user__tokenValue=tokenValue).get(flag=0)
    order.flag = 1
    order.save()

    # 找到属于该订单，被选中的购物车数据,设置为False
    carts = Cart.objects.filter(user__tokenValue=tokenValue).filter(order=order).filter(isCheck=True)
    for cart in carts:
        cart.isOrder = False
        cart.save()
    # 没有被选中的商品生产一个新订单
    neworder = Order.create(str(uuid.uuid4()), User.objects.get(tokenValue=tokenValue), Address.objects.get(pk=1), 0)
    neworder.save()
    # 找到该用户所有没被选中的购物车数据
    oldcart = Cart.objects.filter(user__tokenValue=tokenValue)
    for cart in oldcart:
        cart.order = neworder
        cart.save()
    return JsonResponse({"error": 0})


def mine(request):
    phone = request.session.get("phoneNum", default="未登录")
    # if phone == "未登录":
    #     return redirect('/login/')
    return render(request, "mine/mine.html", {"phone": phone})


import random
import uuid


def login(request):
    if request.method == "GET":
        if request.is_ajax():
            # 验证码
            strNum = '1234567890'
            # 随机选取6个值作为验证码
            rand_str = ''
            for i in range(0, 6):
                rand_str += strNum[random.randrange(0, len(strNum))]
            msg = "您的验证码是：%s。请不要把验证码泄露给其他人。" % rand_str
            phone = request.GET.get("phoneNum")
            # send_sms(msg, phone)
            # 存入session
            request.session["code"] = rand_str
            print("***************", rand_str)
            response = JsonResponse({"data": "ok"})
            return response
        else:
            return render(request, "mine/login.html")
    else:
        phone = request.POST.get("username")
        passwd = request.POST.get("passwd")
        code = request.session.get("code")
        if passwd == code:
            uuidStr = str(uuid.uuid4())
            try:
                user = User.objects.get(pk=phone)
                user.tokenValue = uuidStr
                user.save()
            except User.DoesNotExist as e:
                # 创建用户
                user = User.create(phone, None, uuidStr, "默认头像")
                user.save()
            request.session["phoneNum"] = phone
            response = redirect('/mine/')
            response.set_cookie("token", uuidStr)
            return response
        else:
            return redirect('/login/')


# 商品详情页
def market1(request, pid):
    P = Product.objects.filter(id=pid)
    return render(request, 'market/market1.html', {"P": P})


#
# 退出
from django.contrib.auth import logout


def quit(request):
    logout(request)
    return redirect("/mine/")


# 增加收货地址
def address(request):
    if request.method == "GET":
        return render(request, 'mine/address.html')
    else:
        name = request.POST.get("name")
        sex = request.POST.get("sex")
        if sex == "0":
            sex = False
        sex = True
        phoneNum = request.POST.get("phoneNum")
        postCode = request.POST.get("postCode")
        province = request.POST.get("province")
        city = request.POST.get("city")
        county = request.POST.get("county")
        street = request.POST.get("street")
        detailAddress = request.POST.get("detailAddress")
        address = "province" + "city" + "county" + "street" + "detailAddress"
        phone = request.session.get("phoneNum")
        user = User.objects.get(pk=phone)
        addresses = Address.create(name, sex, phoneNum, postCode, address, province, city, county, street,
                                   detailAddress, user)
        addresses.save()
        return redirect('/showAddress/')


# 展示收货地址
def showAddress(requset):
    addresses = Address.objects.filter(user__phoneNum=requset.session["phoneNum"])
    return render(requset, 'mine/showAddress.html', {"addresses": addresses})
