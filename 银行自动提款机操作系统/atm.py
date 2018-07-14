from user import User
from card import Card
import random
class ATM(object):
    def __init__(self):
        self.allusers={}
    #开户
    def creatUser(self):
        #目标:向用户字典中添加一对键值对(卡号-用户)
        name = input('请输入您的姓名:')
        cardId=input('请输入您的身份证号码:')
        phone=input('请输入您的预存号码:')
        prestoreMoney=input('请输入您的预存金额:')
        if int(prestoreMoney) < 0:
            print('预存款输入有误,开户失败.')
            return -1
        onePassword = input('请设置您的密码:')
        #验证密码:
        if not self.checkPassword(onePassword):
            print('您输入的密码有误,开户失败.')
            return 1
        #所需要的信息齐全
        cardStr=self.randomIdCard()
        card = Card(cardStr ,onePassword , prestoreMoney)
        user = User(name , cardId , phone , card)
        #存到字典字典当中
        self.allusers[cardStr]=user
        print('开户成功!请牢记卡号(%s)******'%(cardStr))
    def searuserInfo(self):
        cardNum = input('请输入卡号:')
        #验证是否存在该银行卡号码.
        user =self.allusers.get(cardNum)
        if not user:
            print('输入的银行卡号码有误!!!查询失败!')
            return -1
        #验证密码
        if not self.checkPassword(user.card.cardPassword):
            print('您输入的密码有误!!!查询失败!')
            return -1
        print('开户成功!您的卡号是%s,您的余额是%d.'%(user.card.cardStr , user.card.cardMoney))

    #取款
    def getMoney(self):
        pass
    #存款
    def setMoney(self):
        pass
    #转账
    def transferMoney(self):
        pass
    #改密
    def TocloseCard(self):
        pass
    #锁定
    def lockCard(self):
        cardNum = input('请输入卡号:')
        user = self.allusers.get(cardNum)
        if not self.allusers.get(cardNum):
            print('输入的银行卡号码有误!!!查询失败!')
            return -1
    #解锁
    def unlockCard(self):
        pass
    #补卡
    def makeCard(self):
        pass
    #销户
    def closeanAccount(self):
        pass
    #验证密码
    def checkPassword(self , realPassword):
        for i in range(3):
            tempPasswprd = input('请输入密码:')
            if tempPasswprd == realPassword :
                return True
        return False
    #随机生成卡号
    def randomIdCard(self):
        while True:
            str = ''
            for i in range(6):
                ch = chr(random.randrange(ord('0'),ord('9')+1))
                str += ch
            if not self.allusers.get(str):
                return str
