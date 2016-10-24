from unittest import TestCase

from builtins import print

from calculations.src.money.functions.insterests import Saldo


class TestSaldo(TestCase):
    def test_income(self):
        saldo = Saldo()
        saldo.income(1)
        self.assertEquals(len(saldo.saldo.keys()), 1)

    def test_interests(self):
         saldo = Saldo()
         self.assertEquals(saldo.interests(1, 50), 0.5)
         self.assertEquals(saldo.interests(1, 0.5), 0.005)

