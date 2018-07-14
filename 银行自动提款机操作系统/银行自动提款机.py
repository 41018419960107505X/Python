'''
人:
类名:Person
属性:姓名 , 身份证号码  , 电话号码
行为:开户 , 取款 , 存款 , 转账 , 改密 , 锁定 , 解锁 , 补卡 , 销户

卡:
类名:Card
属性:卡号 , 密码 , 余额
行为:

界面:
类名:Admin
属性:
行为:管理员界面 , 管理员登录 , 系统功能界面

取款机:
类名:ATM
属性:
行为:开户 ,查询, 取款 , 存款 , 转账 , 改密 , 锁定 , 解锁 , 补卡 , 销户 , 退出
'''
import time
from  view import  Admin
from atm import ATM

def main():
    #界面对象(创建对象)
    admin = Admin()
    #打印管理员界面(调用方法)
    admin.printAdminView()
    if  admin.adminOption():
        return -1
    atm=ATM()
    atm.creatUser()

    #admin.printsysFunctionView()
    while True:
        admin.printsysFunctionView()
        #等待用户的操作:
        option = input('请输入您的操作:')
        if option == '1':
            atm.allusers={}
        elif option == '2':
            atm.searuserInfo()
        elif option == '3':
            print('取款')
        elif option == '4':
            print('存款')
        elif option == '5':
            print('转账')
        elif option == '6':
            print('改密')
        elif option == '7':
            print('锁定')
        elif option == '8':
            print('解锁')
        elif option == '9':
            print('补卡')
        elif option == '0':
            print('销户')
        elif option == 'a':
            if not admin.adminOption():
                return -1
        time.sleep(3)

if __name__=="__main__":
    main()











