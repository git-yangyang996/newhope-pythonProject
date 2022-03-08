import newhope_class
import allure

@allure.feature("创建商品")
class Test_newhope(object):
    @allure.story("登录newhope")
    def setup_class(self):
        newhope_class.Mail.newhope_login(self)
    @allure.story('创建商品')
    def test01(self):
        newhope_class.Mail.newhope_tool_SC_sp(self)
        newhope_class.Mail.newhope_tool_SC_sp_new(self)