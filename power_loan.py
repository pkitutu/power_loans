class PowerLoan(object):
	"""docstring for PowerLoan"""
	__loans = []
	def get_days_of_power(self,**kwargs):
		self.set_loans(kwargs)
		return self.__loans

	def set_loans(self, kwargs):
		self.__loans = [
			{'rate':kwargs.get('R1'),'start_days':kwargs.get('D1')},
			{'rate':kwargs.get('R2'),'start_days':kwargs.get('D2')},
			{'rate':kwargs.get('R3'),'start_days':kwargs.get('D3')},
		]