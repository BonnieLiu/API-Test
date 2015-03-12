import unittest
import json
import requests

class DataCompare(unittest.TestCase):

	def setUp(self):
		self.r = requests.get('http://quote.gf.com.cn/kline/daily/sz/000776/20')


	def test_data_compare(self):
		#request直接将json的字符串转化成一个python的字典
		json_result = self.r.json()

		for data in json_result:
			#print data
			#开始判断low <= avg <= high，如果满足则打印‘pass’，否则则打印‘fail’
			if data['low'] <= data['avg'] <= data['high']:
				print 'pass'
				print 'low:',data['low'] ,'avg:',data['avg'],'high:' ,data['high']
			else:
				print 'fail'
				print 'low:',data['low'] ,'avg:',data['avg'],'high:' ,data['high']


if __name__ == '__main__':
	unittest.main()