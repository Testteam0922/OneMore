#coding:UTF-8

import sys
sys.path.append("..")

from ext import file_read
from conf.gl_config import *
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class Nest_Admin_Add_Hd(unittest.TestCase):
	
	data_file = ".\\test_data\\admin_add_HD.xlsx"
	#读取数据
	listdata = file_read.excel_read(filepath = data_file)	
	
	def setUp(self):
		self.driver = webdriver.Chrome(chromedriver_path)
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get(login_addr)
		time.sleep(2)
		driver.find_element_by_name("username").send_keys(admin_login_name)
		driver.find_element_by_name("password").send_keys(admin_login_passwd)
		driver.find_element_by_xpath("//*[@id='form-validation']/div[5]/button").click()
		time.sleep(2)
	
	def case_run(self,i):
		driver = self.driver		
		self._admin_add_hd(i)
		self.Assertequal(i)

	#用例
	def test_case_00001(self,i=0): self.case_run(i)
		
	#关闭浏览器
	def tearDown(self):
		self.driver.quit()

	def _admin_add_hd(self, i ):
		driver = self.driver
	
		sn = self.listdata[i]["sn"]
		remark = self.listdata[i]["remark"]
			 
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/nav[1]/div[2]/div/div[1]/ul/li[6]/a").click()
		time.sleep(1)
		driver.find_element_by_xpath("/html/body/section/div/div[1]/div/section/div[3]/button[1]").click()
		time.sleep(0.5)
		driver.find_element_by_id("sn_list").send_keys(sn)
		time.sleep(0.5)
		driver.find_element_by_id("remark").send_keys(remark)
		time.sleep(0.5)
		driver.find_element_by_xpath("//*[@id='form-push']/div[2]/button[2]").click()
		

	#断言
	def Assertequal(self, i):
		driver = self.driver
		xpath = self.listdata[i]["xpath"]
		expectValue=self.listdata[i]['expectValue']
		print u"expectValue:" + expectValue
		try:
			time.sleep(1)
			actualValue = driver.find_element_by_xpath(xpath).text
			print u"actualValue:" + actualValue
			#判断预期与实际结果是否相等，为真通过，为假截图
			vlue = self.assertCompare(expectValue,actualValue)
			if vlue:
				pass
			else:
				fail_pic_path = case_pic_path + "Nest_Admin_Add_Hd_%s.png"%(i+1)
				print "image" + fail_pic_path
				driver.get_screenshot_as_file(fail_pic_path)
				assert 0,u"~~~~~~Test Case Fail~~~~~~"				
		except NoSuchElementException:
			fail_pic_path = case_pic_path + "Nest_Admin_Add_Hd_%s.png"%(i+1)
			print "image" + fail_pic_path
			driver.get_screenshot_as_file(fail_pic_path)
			assert 0,u"~~~~~~xpath not exist~~~~~~"
		time.sleep(1)

	#预期与实际比较
	def assertCompare(self,expectValue,actualValue):
		flag=True
		driver = self.driver	
		try:
			self.assertEqual(expectValue, actualValue)
			return flag
		except:
			flag=False
			return flag