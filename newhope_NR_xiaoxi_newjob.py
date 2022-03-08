import newhope_class
import allure

@allure.feature("创建消息推送")
class Test_newhope(object):
    @allure.story("登录newhope")
    def setup_class(self):
        newhope_class.Mail.newhope_login(self)
    @allure.story('新建消息推送-默认')
    def test01(self):
        newhope_class.Mail.newhope_tool_NR_xiaoxi(self)
        newhope_class.Mail.newhope_tool_NR_xiaoxi_new(self)