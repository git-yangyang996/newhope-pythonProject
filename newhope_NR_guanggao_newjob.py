import os
import pytest
import newhope_class
import allure

@allure.feature("创建广告")
class Test_newhope(object):
    @allure.story("登录newhope")
    def setup_class(self):
        newhope_class.Mail.newhope_login(self)

    @allure.story("新建广告")
    def test01(self):
        self.driver.implicitly_wait(30)
        newhope_class.Mail.newhope_tool_NR_guangg(self)
        newhope_class.Mail.newhope_tool_NR_guangg_new(self)

if __name__=='__main__':
    pytest.main(['--alluredir','C:/Users/86173/PycharmProjects/pythonProject/testlog'])
    os.system('allure generate C:/Users/86173/PycharmProjects/pythonProjecttestlog -o C:/Users/86173/PycharmProjects/pythonProject/report --clean')





