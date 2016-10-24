import datetime

class Saldo:
    '''
    saldo
    operacje na saldo= [kwota, data]
    okresy rozliczeniowe = naliczanie odsetek
    stopa procentowa
    okres = [początek naliczania] do [koniec naliczania]

    '''
    def __init__(self):
        self.saldo = {}

    '''
    Method increases saldo
        value has to be positive
        else method has no effect
    '''

    def income(self, value, date=None):
        if value < 0:
            return
        self.saldo[datetime.datetime.now()]=value


    '''
    Method decreases saldo
        value has to be negative
        else method has no effect
    '''
    def outcome(self, value):
        if value > 0:
             return
        self.operations.append(-value)

    def interests(self, value, percent):
        return value * percent/100

class InterestConfiguration:
    def __init__(self):
        self.interstAmount = 0
        self.interestCalculationType = 0
        self.interestDuration = 0


