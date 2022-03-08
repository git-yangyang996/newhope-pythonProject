import newhope_class
import allure

@allure.feature("创建业主活动")
class Test_newhope(object):
    @allure.story("登录newhope")
    def setup_class(self):
        newhope_class.Mail.newhope_login(self)

    @allure.story("创建业主活动")
    def test01(self):
        self.driver.implicitly_wait(30)
        newhope_class.Mail.newhope_tool_HD_yz(self)
        newhope_class.Mail.newhope_tool_HD_yz_new(self)