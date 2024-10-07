import unittest
from wqi_calculator import WQICalculator

class TestQWICalculator(unittest.TestCase):
	def test_wqi_evaluation(self):
		calculator = WQICalculator(ph=7., tds=400, tur=3., do=7.)
		wqi_result = calculator.evaluate_wqi()
		self.assertEqual(wqi_result, "Excellent quality")

if __name__ == '__main__':
	unittest.main()
