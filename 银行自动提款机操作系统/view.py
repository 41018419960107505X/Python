import time
class Admin(object):
    admin   = '1'
    passord = '1'
    def printAdminView(self):
        print("******************************************************")
        print("**                                                  **")
        print("**                                                  **")
        print("**                                                  **")
        print("**               欢迎登陆中国建设银行                  **")
        print("**                                                  **")
        print("**                                                  **")
        print("**                                                  **")
        print("******************************************************")


    def printsysFunctionView(self):
        print("******************************************************")
        print("**          开户(1)          查询(2)                 **")
        print("**          取款(3)          存款(4)                 **")
        print("**          锁定(7)          解锁(8)                 **")
        print("**          转账(5)          改密(6)                 **")
        print("**          补卡(9)          销户(0)                 **")
        print("**                  退出(a)                         **")
        print("******************************************************")

    def adminOption(self):
        inputAnmin = input('请输入管理员账号:')
        if self.admin != inputAnmin:
            print('您输入的管理员账号有误!请重新输入.')
            return -1

        inputPassord = input('请输入您的密码:')
        if self.passord != inputPassord:
            print('您输入的管理员密码有误!请重新输入.')
            return -1

        print('操作成功!请稍后......')
        time.sleep(3)
        return 0


















