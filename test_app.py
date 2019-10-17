import math
"""
Author: Kitutu Paul
Oct, 2019
"""

import unittest
from power_loan import PowerLoan

class TestPowerLoan(unittest.TestCase):
	"""
	p1 - 4+3+math.floor( (700000-(3000*4 + 4500*3))/5000) == 141
	p2 - 4+3+math.floor((21000-(500*4+1000*3))/1500) == 17
	p3 - math.floor(10000/1800) == 5
	p4 - math.floor(11000/10000) == 1
	"""
	powerloan1 = PowerLoan()
	powerloan2 = PowerLoan()
	powerloan3 = PowerLoan()
	powerloan4 = PowerLoan()
	def test_get_days_of_power(self):
		self.assertEqual(self.powerloan1.get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000), 141)
		self.assertEqual(self.powerloan2.get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000), 17)
		self.assertEqual(self.powerloan3.get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000),5)
		self.assertEqual(self.powerloan4.get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000),1)

if __name__ == '__main__':
	unittest.main()