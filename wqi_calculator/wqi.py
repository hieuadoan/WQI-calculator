class WQICalculator:
	"""
	A calculator class for water quality index

	Inputs: ph -- pH value
			tds -- total dissolved solid
			tur -- turbidity
			do -- dissolved oxygen

	Outputs: Index score {4: 'excellent', 3: 'good', 2: 'fair', 1:'poor'}
	"""
	def __init__(self, ph, tds, tur, do):
		self.ph = ph
		self.tds = tds
		self.tur = tur
		self.do = do 

	def evaluate_wqi(self):
		ph_score = self._ph_score(self.ph)
		tds_score = self._tds_score(self.tds)
		tur_score = self._tur_score(self.tur)
		do_score = self._do_score(self.do)
		wqi = (ph_score + tds_score + tur_score + do_score)/4.
		
		if wqi >= 3.5:
			return 'Excellent quality'
		elif wqi >= 3.:
			return 	'Good quality'
		elif wqi >= 2.:
			return 'Fair quality'
		else:
			return 'Poor quality'

	def _ph_score(self, ph):
		if ph >= 6.5 and ph <= 8.5:
			return 4.
		elif ph >= 6 and ph <= 9:
			return 3.
		elif ph >=5 and ph <= 10:
			return 2.
		else: 
			return 1.

	def _tds_score(self, tds):
		if tds <= 500:
			return 4.
		elif tds <= 1000:
			return 3.
		elif tds <= 1500:
			return 2.
		else:
			return 1.

	def _tur_score(self, tur):
		if tur <= 5:
			return 4.
		elif tur <= 10:
			return 3.
		elif tur <= 50:
			return 2.
		else: 
			return 1.

	def _do_score(self, do):
		if do >=6:
			return 4.
		elif do >=5:
			return 3.
		elif do >=3:
			return 2.
		else: 
			return 1.

if __name__ == '__main__':
	calculator = WQICalculator(7.0, 400, 3, 7)
	result = calculator.evaluate_wqi()
	print(result)
