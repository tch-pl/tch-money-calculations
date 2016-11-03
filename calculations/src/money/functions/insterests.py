import datetime
from enum import Enum

class Saldo:
    '''
    saldo
    operacje na saldo= [kwota, data]

    '''

    def __init__(self):
        self.saldo = {}

    '''
    Method increases saldo
        value has to be positive
        else method has no effect
    '''

    def income(self, value, date=None):
        if value < 0 or date is None:
            return
        self.saldo[datetime.datetime.now()] = value

    '''
    Method decreases saldo
        value has to be negative
        else method has no effect
    '''

    def outcome(self, value, date=None):
        if value > 0 or date is None:
            return
        self.saldo[datetime.datetime.now()] = value

    def saldo(self, value, percent):
        total = 0
        for v in self.saldo.values():
            total += v
        return total


class Interests:
    '''
    okresy rozliczeniowe = naliczanie odsetek
    stopa procentowa
    okres = [początek naliczania] do [koniec naliczania]
    '''

    def __init__(self):
        self.interstAmount = 0
        self.interestCalculationType = InterestsCalculationType.monthly
        self.interestDuration = 0
        self.interestStartDate = None

    '''
    zwraca daty kiedy naliczane sa odsetki
    '''
    def chargeDates(self):
        if self.interestCalculationType == InterestsCalculationType.monthly:
            pass
        elif self.interestCalculationType == InterestsCalculationType.daily:
            pass
        elif self.interestCalculationType == InterestsCalculationType.yearly:
            pass
        return []

    '''
    oblicza wartosc powiekszona o odsetki
    '''
    def plusInterests(self, value):
        return value * self.interstAmount / 100


class InterestsCalculationType(Enum):
    daily = 'daily'
    monthly = 'monthly'
    yearly = 'yearly'