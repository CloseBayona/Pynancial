import unittest
from Financier.Invester import interestRate

class TestInterest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.interest = interestRate.interestRateOfReturn(116, 105)
        self.simple = self.interest.simple()
        self.logarithmic = self.interest.logarithmic()

    def test_sInterestRate(self):

        self.assertEqual(self.simple, 0.10476190476190476)

    def test_lInterestRate(self):

        self.assertEqual(self.logarithmic, 0.09962984094884134)