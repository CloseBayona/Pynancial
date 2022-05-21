import unittest
from Financier.Invester import interestRate

class TestInterest(unittest.TestCase):

    def setUp(self) -> None:
        
        self.sInterestRate = interestRate.sInterestRate(116, 105)

    def test_sInterestRate(self):

        self.assertEqual(self.sInterestRate, 0.10476190476190476)