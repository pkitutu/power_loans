import math
"""
Author: Kitutu Paul
Oct, 2019
"""

import unittest
from power_loan import PowerLoan

class TestPowerLoan(unittest.TestCase):
	"""
	4+3+math.floor( (700000-(3000*4 + 4500*3))/5000) == 141
	4+3+math.floor((21000-(500*4+1000*3))/1500) == 17
	math.floor(10000/1800)
	math.floor(11000/10000)
	"""
	powerloan = PowerLoan()
	def test_get_days_of_power(self):
		self.assertEqual(powerloan.get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000), 141)
		self.assertEqual(powerloan.get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000), 17)
		self.assertEqual(powerloan.get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000),5)
		self.assertEqual(powerloan.get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000),1)

if __name__ == '__main__':
	unittest.main()



