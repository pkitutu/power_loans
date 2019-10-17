import math
class PowerLoan(object):
	"""docstring for PowerLoan"""
	__loans = []
	__soonest_days = None
	__nxt_soonest_days = None
	__soonest_loans = []
	__my_balance = 0
	__current_daily_rate = 0
	def get_days_of_power(self,**kwargs):
		self.__my_balance = kwargs.get('K')
		self.set_loans(kwargs)
		return self.get_days()

	def get_days(self):
		self.set_soonest()		
		self.set_daily_rate()
		duration = self.get_duration()
		due_amount = self.get_due_amount(duration)

		if self.__nxt_soonest_days is None or self.__my_balance<=due_amount:
			#How long can what I've take based on my current daily rate
			return math.floor(self.__my_balance/self.__current_daily_rate)
		else:
			self.__my_balance -= due_amount
			return duration+self.get_days() 


	def set_loans(self, kwargs):
		self.__loans = [
			{'rate':kwargs.get('R1'),'start_days':kwargs.get('D1')},
			{'rate':kwargs.get('R2'),'start_days':kwargs.get('D2')},
			{'rate':kwargs.get('R3'),'start_days':kwargs.get('D3')},
		]
	
	def set_soonest(self):
		#sets the soonest start days, soonest loans and next soonest start days
		self.__soonest_days = self.get_min_start_days()
		self.set_soonest_loans()
		self.remove_soonest_loans()
		self.__nxt_soonest_days = self.get_min_start_days()

	def set_soonest_loans(self):
		self.__soonest_loans = [loan for loan in self.__loans if loan.get('start_days') == self.__soonest_days]

	def get_duration(self):
		return self.__nxt_soonest_days-self.__soonest_days if self.__nxt_soonest_days is not None else 0

	def remove_soonest_loans(self):
		self.__loans = [loan for loan in self.__loans if loan not in self.__soonest_loans]

	def get_min_start_days(self):
		return min([loan.get('start_days') for loan in self.__loans]) if len(self.__loans)>0 else None

	def set_daily_rate(self):
		self.__current_daily_rate += sum([loan.get('rate') for loan in self.__soonest_loans])

	def get_due_amount(self, duration):
		return duration*self.__current_daily_rate