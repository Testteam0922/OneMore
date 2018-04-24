# coding=utf-8

import sys
sys.path.append("..")

import urllib
import unittest
import re
import time


from tools import file_read
from tools.key_value_sign import *
from tools.req import *

class returnCode_pay_query(unittest.TestCase):
	# 读取文件
	data_file = '.\\test_data\\returnCode_pay_query.xlsx'
	url = "http://103.36.132.29:8080/mpip-gateway/query/orderquery"
	datalist = file_read.excel_table_value(filepath = data_file)
	data_key = ['mch_id','agent_id','v','timestamp','mch_trade_no','mpip_no','third_no','sign_type']
	

	def case_action(self, i): 
		clean_data = self._clean_data(self.datalist[i])
		payload = self._get_payload(clean_data)
		res = self.send_request(payload,clean_data)
		self.resultsComparison(res,clean_data)

	#初始化数据参数
	def _clean_data(self, data):
		for key, value in data.items():
			data[key] = value
		return data	

	def _get_payload(self,clean_data):
		params = {}
		
		print u'用例说明: ' + clean_data['note']
		
		for key in self.data_key: #获取除body外的其它参数
			if clean_data[key] == "null":	#当需要不传这个键值对是，在数据文件中填入null
				continue
			elif (clean_data[key] == "time"):  #当数据文件中该字段的值为time时，使用时间格式代替
				now  = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
				clean_data[key] = now
				params.update({key.encode('utf-8'):clean_data[key].encode('utf-8')})
			else:
				params.update({key.encode('utf-8'):clean_data[key].encode('utf-8')})
		print self.url
		print params	
		return params
		

	#获取签名			
	def get_sign(self,payload,key):
		return get_key_value_sign(payload, key)


	#发送请求
	def send_request(self,payload,clean_data):
		headers = {}
		sign_value = self.get_sign(payload,clean_data['sign_key'].encode('utf-8'))
		payload["sign"] = sign_value
		res = req("GET", self.url, headers, payload)
		print u'返回结果: '+ res
		return res
		
	
	#匹配字段，验证结果
	def resultsComparison(self, actual_results,i):
		expected_data  = self.expected_outcome_data(i)
		no = 0
		success = []
		for i in range(len(expected_data)):
			pattern = re.compile(expected_data[i])
			match = pattern.search(actual_results)
			if match:
				pass
#				success.append(match.group())
			else:
				print u'参数: ' + expected_data[i] + u' 匹配失败'
				no = no + 1
#		print success
		self.assertEqual(0, no)
	
	
	#获取预期结果
	def expected_outcome_data(self,clean_data):
		expected_value = clean_data['expected_outcome_data']
		expected_value_list = expected_value.split(",")
		return expected_value_list


	def test_case_001	(self,i=1): self.case_action(i)
	def test_case_002	(self,i=2): self.case_action(i)
	def test_case_003	(self,i=3): self.case_action(i)
	def test_case_004	(self,i=4): self.case_action(i)
	def test_case_005	(self,i=5): self.case_action(i)
	def test_case_006	(self,i=6): self.case_action(i)
	def test_case_007	(self,i=7): self.case_action(i)
	def test_case_008	(self,i=8): self.case_action(i)
	def test_case_009	(self,i=9): self.case_action(i)
	def test_case_010	(self,i=10): self.case_action(i)
	def test_case_011	(self,i=11): self.case_action(i)
	def test_case_012	(self,i=12): self.case_action(i)
	def test_case_013	(self,i=13): self.case_action(i)
	def test_case_014	(self,i=14): self.case_action(i)
	def test_case_015	(self,i=15): self.case_action(i)
	def test_case_016	(self,i=16): self.case_action(i)
	def test_case_017	(self,i=17): self.case_action(i)
	def test_case_018	(self,i=18): self.case_action(i)
	def test_case_019	(self,i=19): self.case_action(i)
	def test_case_020	(self,i=20): self.case_action(i)
	def test_case_021	(self,i=21): self.case_action(i)
	def test_case_022	(self,i=22): self.case_action(i)
	def test_case_023	(self,i=23): self.case_action(i)
	def test_case_024	(self,i=24): self.case_action(i)
	def test_case_025	(self,i=25): self.case_action(i)
	def test_case_026	(self,i=26): self.case_action(i)
	def test_case_027	(self,i=27): self.case_action(i)
	def test_case_028	(self,i=28): self.case_action(i)
	def test_case_029	(self,i=29): self.case_action(i)
	def test_case_030	(self,i=30): self.case_action(i)
	def test_case_031	(self,i=31): self.case_action(i)
	def test_case_032	(self,i=32): self.case_action(i)
	def test_case_033	(self,i=33): self.case_action(i)
	def test_case_034	(self,i=34): self.case_action(i)
	def test_case_035	(self,i=35): self.case_action(i)
	def test_case_036	(self,i=36): self.case_action(i)
	def test_case_037	(self,i=37): self.case_action(i)
	def test_case_038	(self,i=38): self.case_action(i)
	def test_case_039	(self,i=39): self.case_action(i)
	def test_case_040	(self,i=40): self.case_action(i)
	def test_case_041	(self,i=41): self.case_action(i)
	def test_case_042	(self,i=42): self.case_action(i)
	def test_case_043	(self,i=43): self.case_action(i)
	def test_case_044	(self,i=44): self.case_action(i)
	def test_case_045	(self,i=45): self.case_action(i)
	def test_case_046	(self,i=46): self.case_action(i)
	def test_case_047	(self,i=47): self.case_action(i)
	def test_case_048	(self,i=48): self.case_action(i)
	def test_case_049	(self,i=49): self.case_action(i)
	def test_case_050	(self,i=50): self.case_action(i)
	def test_case_051	(self,i=51): self.case_action(i)
	def test_case_052	(self,i=52): self.case_action(i)
	def test_case_053	(self,i=53): self.case_action(i)
	def test_case_054	(self,i=54): self.case_action(i)
	def test_case_055	(self,i=55): self.case_action(i)
	def test_case_056	(self,i=56): self.case_action(i)
	def test_case_057	(self,i=57): self.case_action(i)
	def test_case_058	(self,i=58): self.case_action(i)
	def test_case_059	(self,i=59): self.case_action(i)
	def test_case_060	(self,i=60): self.case_action(i)
	def test_case_061	(self,i=61): self.case_action(i)