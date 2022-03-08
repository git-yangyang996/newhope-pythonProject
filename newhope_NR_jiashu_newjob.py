import os
import pytest
import newhope_class
import allure

@allure.feature("创建家书")
class Test_newhope(object):
    @allure.story("登录newhope")
    def setup_class(self):
        newhope_class.Mail.newhope_login(self)
    @allure.story('新建家书')
    def test01(self):
        newhope_class.Mail.newhope_tool_NR_jiashu(self)
        newhope_class.Mail.newhope_too_NR_jiashu_new(self)