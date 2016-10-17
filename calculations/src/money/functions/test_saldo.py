from unittest import TestCase

from builtins import print

from calculations.src.money.functions.insterests import Saldo


class TestSaldo(TestCase):
    def test_income(self):
        saldo = Saldo()
        saldo.income(1)
        print(saldo.saldo)

