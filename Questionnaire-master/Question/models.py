from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    """
    # 客户信息
    """
    user = models.OneToOneField(User)
    name = models.CharField(default='名称', max_length=32, help_text="客户名称")
    email = models.EmailField(default='', null=True,
                              blank=True, help_text="邮箱")
    company = models.CharField(
        default='', max_length=32, null=True, blank=True, help_text="公司名称")
    address = models.CharField(
        default='', max_length=256, null=True, blank=True, help_text="地址")
    phone = models.CharField(default='', max_length=16,
                             blank=True, null=True, help_text="手机号码")
    mobile = models.CharField(
        default='', max_length=16, blank=True, null=True, help_text="座机")
    qq = models.CharField(default='', max_length=16,
                          null=True, blank=True, help_text="QQ")
    wechat = models.CharField(
        default='', max_length=64, null=True, blank=True, help_text="微信号")
    web = models.CharField(default='', max_length=64,
                           blank=True, null=True, help_text="网站地址")
    industry = models.CharField(
        default='', max_length=32, blank=True, null=True, help_text="行业")
    description = models.TextField(
        default='', null=True, blank=True, help_text="公司简介")

    @classmethod
    def create_customer(cls, user, **kwargs):
        customer = Customer.objects.create(user=user, **kwargs)
        wallet = Wallet.objects.create(customer=customer, balance=0)


class UserInfo(models.Model):
    """
    # 用户信息
    """
    user = models.OneToOneField(User)
    name = models.CharField(default='姓名', max_length=32, help_text="姓名")
    age = models.IntegerField(default=1, help_text="年龄")
    gender = models.CharField(max_length=8, default="male", help_text="性别")
    phone = models.CharField(default='', max_length=16,
                             blank=True, null=True, help_text="手机号码")
    email = models.EmailField(default='', blank=True,
                              null=True, help_text="邮箱")
    address = models.CharField(
        default='', max_length=256, blank=True, null=True, help_text="地址")
    birthday = models.DateField(default=date(
        2018, 1, 1), null=True, help_text="出生日期")
    qq = models.CharField(default='', max_length=16,
                          blank=True, null=True, help_text="QQ")
    wechat = models.CharField(
        default='', max_length=64, blank=True, null=True, help_text="微信号")
    job = models.CharField(default='', max_length=32,
                           blank=True, null=True, help_text="职业")
    salary = models.CharField(
        default='', max_length=32, blank=True, null=True, help_text="收入水平")

    @classmethod
    def create_userinfo(cls, user, **kwargs):
        userinfo = UserInfo.objects.create(user=user, **kwargs)
        point = Point.objects.create(userinfo=userinfo, balance=0)


class Point(models.Model):
    """
    # 用户积分
    """
    userinfo = models.OneToOneField('UserInfo', help_text="用户信息")
    balance = models.IntegerField(default=0, help_text="余额")

    # 更新积分
    @classmethod
    def update_point(cls, userinfo, amount=0, reason='未提供'):
        """
        userinfo: 用户对象
        amount: 积分变动数量
        """
        # 更新积分
        user_point = userinfo.point
        balance = user_point.balance+amount
        if balance > 0:
            user_point.balance = balance
        else:
            return False
        user_point.save()
        # 保存历史记录
        PointHistory.objects.create(
            point=user_point, quantity=amount, reason=reason, direction=True if amount > 0 else False)
        return True


class PointHistory(models.Model):
    """
    # 积分历史
    """
    point = models.ForeignKey('Point', help_text="积分")
    create_date = models.DateTimeField(auto_now=True, help_text="发生时间")
    quantity = models.IntegerField(default=0, help_text="数量")
    reason = models.CharField(max_length=32, help_text="变动原因")
    direction = models.BooleanField(
        default=True, help_text="方向,增加为True,减少为False")


class SignHistory(models.Model):
    """
    # 签到记录
    """
    userinfo = models.ForeignKey('UserInfo', help_text="用户信息")
    create_date = models.DateTimeField(auto_now=True, help_text="签到时间")


class Wallet(models.Model):
    """
    # 客户钱包
    """
    customer = models.OneToOneField('Customer', help_text="客户")
    balance = models.IntegerField(default=0, help_text="余额")

    # 更新钱包金额
    @classmethod
    def update_wallet(cls, customer, amount=0, reason='未提供'):
        """
        customer: 客户对象
        amount: 金额变动数量
        """
        # 更新积分
        wallet = customer.wallet
        balance = wallet.balance+amount
        if balance > 0:
            wallet.balance = balance
        else:
            return False
        wallet.save()
        # 保存历史记录
        WalletFlow.objects.create(wallet=wallet,
                                  amount=amount, reason=reason, direction=True if amount > 0 else False)
        return True


class WalletFlow(models.Model):
    """
    # 钱包流水明细
    """
    wallet = models.ForeignKey('Wallet', help_text="钱包")
    amount = models.IntegerField(default=0, help_text="发生金额")
    direction = models.BooleanField(
        default=True, help_text="方向,增加为True,减少为False")
    create_date = models.DateTimeField(auto_now=True, help_text="发生时间")
    reason = models.CharField(max_length=32, help_text="变动原因")
    done = models.BooleanField(default=False, help_text="是否已完成")
    payment = models.CharField(max_length=32, choices=[(
        'alipay', '支付宝'), ('wechat', '微信')], help_text="支付方式")
    paymentid = models.CharField(max_length=128, help_text="第三方支付id")


class Questionnaire(models.Model):
    """
    # 问卷
    """
    customer = models.ForeignKey('Customer', help_text="客户信息")
    title = models.CharField(default="标题", max_length=64, help_text="标题")
    create_date = models.DateTimeField(help_text="创建时间")
    deadline = models.DateTimeField(help_text="截止时间")
    state = models.IntegerField(default=0, help_text="""状态,0-->草稿,1-->待审核,2-->审核失败,
                                                        3-->审核成功,4-->发布成功""")
    quantity = models.IntegerField(default=1, help_text='发布数量')
    free_count = models.IntegerField(default=1, help_text='可用问卷数量')


class QuestionnaireComment(models.Model):
    """
    # 问卷审核
    """
    questionnaire = models.ForeignKey(
        'Questionnaire', help_text="问卷", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True, help_text="审核时间")
    comment = models.TextField(help_text="审核批注")


class Question(models.Model):
    """
    # 题目
    """
    category_choices = [
        ('radio', '单选'),
        ('select', '多选'),
    ]
    questionnaire = models.ForeignKey(
        'Questionnaire', help_text="问卷", on_delete=models.CASCADE)
    title = models.CharField(max_length=128, help_text="题纲")
    index = models.IntegerField(default=0, help_text="题目题号", db_index=True)
    category = models.CharField(
        choices=category_choices, default='radio', max_length=16, help_text="是否多选")


class QuestionItem(models.Model):
    """
    # 题目选项
    """
    question = models.ForeignKey(
        'Question', help_text="题目", on_delete=models.CASCADE)
    content = models.CharField(max_length=32, help_text="选项内容")


class Mark(models.Model):
    """
    # 标签
    """
    name = models.CharField(max_length=8, help_text="标签名称")
    description = models.TextField(default="", help_text="介绍")


class ShareHistory(models.Model):
    """
    # 分享历史
    """
    userinfo = models.ForeignKey('UserInfo', help_text=" 用户信息")
    questionnaire = models.ForeignKey('Questionnaire', help_text="问卷")
    create_date = models.DateTimeField(auto_now=True, help_text="分享时间")
    url = models.CharField(max_length=128, default='',
                           blank=True, null=True, help_text="分享链接")
    # 关联到Image
    qrcode = models.CharField(max_length=32, null=True,
                              blank=True, help_text="分享二维码")


class Answer(models.Model):
    """
    # 回答问卷题目
    """
    userinfo = models.ForeignKey('UserInfo', null=True, help_text="用户信息")
    questionnaire = models.ForeignKey('Questionnaire', help_text="问卷")
    create_date = models.DateTimeField(auto_now=True, help_text="参与时间")
    is_done = models.BooleanField(default=False, help_text="是否已经完成")


class AnswerItem(models.Model):
    """
    # 回答题目选项
    """
    userinfo = models.ForeignKey('UserInfo', null=True, help_text="用户信息")
    item = models.ForeignKey('QuestionItem', help_text="选项")


class QuestionnaireSuggest(models.Model):
    """
    # 问卷建议
    """
    userinfo = models.ForeignKey('UserInfo', null=True, help_text="用户信息")
    questionnaire = models.ForeignKey('Questionnaire', help_text="问卷")
    create_date = models.DateTimeField(auto_now=True, help_text="提交时间")
    comment = models.TextField(default='', help_text="建议内容")
