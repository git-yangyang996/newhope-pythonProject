import newhope_data
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime


class os(object):
    # 获取系统时间
    ostime = datetime.datetime.now()
    time = ostime.strftime('%Y-%m-%d %H:%M:%S')
    time_date = ostime.strftime('%Y-%m-%d')
    time_date_d = ostime.strftime('%d')
    minu01 = 20
    minu02 = minu01 + 120
    minu_bm_01 = 1
    minu_bm_02 = minu_bm_01 + 9
    minu_ms_01 = 2
    minu_ms_02 =  20
    ostime_start = (ostime + datetime.timedelta(minutes=minu01)).strftime('%Y-%m-%d %H:%M:%S')
    ostime_end = (ostime + datetime.timedelta(minutes=minu02)).strftime('%Y-%m-%d %H:%M:%S')
    ostime_BM_start = (ostime + datetime.timedelta(minutes=minu_bm_01)).strftime('%Y-%m-%d %H:%M:%S')
    ostime_BM_end = (ostime + datetime.timedelta(minutes=minu_bm_02)).strftime('%Y-%m-%d %H:%M:%S')
    ostime_ms_start = (ostime + datetime.timedelta(hours=1)).strftime('%H:%M:%S')
    ostime_ms_end = (ostime + datetime.timedelta(hours=8)).strftime('%H:%M:%S')


class Mail:

    def newhope_login(self):#登录newhope
        chrom_driver = 'C:/Users/86173/AppData/Local/Google/Chrome/Application/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrom_driver)
        self.driver.get(newhope_data.new_hope_url)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(newhope_data.web_login_user).send_keys(newhope_data.user)
        self.driver.find_element_by_xpath(newhope_data.web_login_pass).send_keys(newhope_data.password)
        self.driver.find_element_by_xpath(newhope_data.web_login_querne).click()

    def newhope_sql_login(self):#登录线上sql
        chrom_driver = 'C:/Users/86173/AppData/Local/Google/Chrome/Application/chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=chrom_driver)
        self.driver.get(newhope_data.newhope_sql)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_use).send_keys('yangyang')
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_password).send_keys('Yangy#0901')
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_login).click()

    def newhope_sql_redis_select(self):
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_SL).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_SL_redis).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_ku).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_ku_5).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_select).send_keys(Keys.TAB)
        self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_select_txt).send_keys('get customer:mobile:verify-code:')
        #self.driver.find_element_by_xpath(newhope_data.newhope_sql_CX_zx_select).send_keys('get customer:mobile:verify-code:')



    def newhope_tool_sy(self):#进入首页页面
        self.driver.find_element_by_xpath(newhope_data.newhope_sy).click()

    def newhope_tool_NR_guangg(self):#进入广告页面
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg).click()

    def newhope_tool_NR_guangg_new(self):#新建广告
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_name).send_keys("new广告01")
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_lanmu).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_lanmu_shouye).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_weizhi).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_weizhi_lunbo).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_riqi).send_keys(os.time_date)
        time.sleep(3)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_png).send_keys("C:/Users/86173/Pictures/Saved Pictures/1645434415379.jpg")
        time.sleep(5)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_guangg_newjob_tijiao).click()

    def newhope_tool_NR_jiashu(self):#进入家书页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu).click()

    def newhope_too_NR_jiashu_new(self):#新建家书
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_name).send_keys('Test家书name')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_neirong).send_keys('Test家书内容')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_city).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_city_cd).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_project).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_project_JGG).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_data).send_keys(os.time_date)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_png).send_keys('C:/Users/86173/Pictures/Saved Pictures/1645434415379.jpg')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_png_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_html).send_keys('Test家书连接')
        time.sleep(3)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_jiashu_newjob_ok).click()

    def newhope_tool_NR_xiaoxi(self):#进入消息页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_xiaoxi).click()

    def newhope_tool_NR_xiaoxi_new(self):  #新建消息
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_xiaoxi_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_xiaoxi_newjob_name).send_keys(
            'Test消息name')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_xiaoxi_newjob_neirong).send_keys(
            'Test消息内容')
        time.sleep(3)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_neirong_xiaoxi_newjob_ok).click()

    def newhope_tool_SC_sp(self):#进入积分商品界面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP).click()

    def newhope_tool_SC_ms(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS).click()

    def newhope_tool_SC_sp_new(self):#新建商品
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_name).send_keys(
            'Test商品name')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_leixin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_leixin_xunni).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_shuoshu).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_shuoshu_jifen).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_title).send_keys('Test副标题内容')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_shichang).send_keys('100')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_cb).send_keys('50')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_kuchun).send_keys('100')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_duihuan).send_keys('10')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_png).send_keys(newhope_data.os_png)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_neirong).send_keys('Test商品内容')
        time.sleep(3)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_jifenSP_newjob_ok).click()

    def newhope_tool_SC_ms_new(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob_name).send_keys('秒杀title')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob_starttime).send_keys(os.ostime_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob_endtime).send_keys(os.ostime_end)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_name).send_keys(os.ostime_ms_start,"秒杀")
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_startime).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_startime).clear()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_startime).send_keys(os.ostime_ms_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_startime).send_keys(Keys.TAB)
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_endtime).clear()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_endtime).send_keys(os.ostime_ms_end)
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob2_save).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp_01).click()
        time.sleep(10)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp_xg).send_keys('5')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp_mssl).send_keys('5')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob3_mssp_newsp_closs).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_shangchen_MS_newjob4_ok).click()




    def newhope_tool_HD_yx(self):#进入活动营销页面
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX).click()

    def newhope_tool_HD_yx_new(self):
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_name).send_keys('Test营销活动时间')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_png).send_keys(newhope_data.os_png)
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_png_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_timestrat).send_keys(os.ostime_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_timeend).send_keys(os.ostime_end)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_timetx).send_keys(os.time)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_nr).send_keys('Test营销活动内容')
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob_ok).click()

        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob2_timestart).send_keys(os.ostime_BM_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob2_timeend).send_keys(os.ostime_BM_end)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob2_BM).send_keys("5")
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob2_XE).send_keys('5')
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YX_newjob2_ok).click()

    def newhope_tool_HD_yz(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ).click()

    def newhope_tool_HD_yz_new(self):
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_name).send_keys('Test业主活name')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_png).send_keys(newhope_data.os_png)
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_png_ok).click()
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_timestart).send_keys(os.ostime_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_timeend).send_keys(os.ostime_end)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_txtime).send_keys(os.ostime_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_NR).send_keys('Test业主活动简介')
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new_ok).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new2_timestart).send_keys(os.ostime_BM_start)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new2_timesend).send_keys(os.ostime_BM_end)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new2_BM).send_keys('5')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new2_CY).send_keys('5')
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new2_ok).click()
        time.sleep(1)
        self.driver.find_element_by_xpath(newhope_data.newhope_yunyin_huodong_YZ_new3_ok).click()




















