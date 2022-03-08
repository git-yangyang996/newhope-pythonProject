import newhope_class
import allure

class Test_newhope(object):
    @allure.story("登录newhope sql")
    def setup_class(self):
        newhope_class.Mail.newhope_sql_login(self)

    @allure.story("redis查询")
    def test01(self):
        self.driver.implicitly_wait(30)
        newhope_class.Mail.newhope_sql_redis_select(self)
