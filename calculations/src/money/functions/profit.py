from __future__ import division
import calendar

DURATION_ENUM = {"month":12, "day":365, "end":1}

class Deposit:
    def __init__(self, saldo=0, interest=0, duration=0):
        self.saldo = saldo
        self.interest = interest
        self.duration = duration
        self.capitalisation_key="month"
        self.capitalisation = DURATION_ENUM[self.capitalisation_key]
    
    def normalize_capitalisation(self, interest, capitalisation):
        return (interest/capitalisation)/100
    
    def calculate_profit(self, saldo):
        interest = self.normalize_capitalisation(self.interest, self.capitalisation)
        return (saldo*interest)
    
    def daily_profit(self, saldo):
        capitalisation_key="day"
        capitalisation = DURATION_ENUM[capitalisation_key]
        interest = self.normalize_capitalisation(self.interest, capitalisation)
        return interest*saldo
        
    def monthly_profit(self, days, saldo):
        profit = 0
        for i in range(0, days):
            profit += self.daily_profit(saldo)
        return profit
    
    def calculate_total_profit(self, saldo):
        if self.capitalisation_key=="month":
            for i in range(0,self.duration):
                saldo+=self.monthly_profit(30, saldo)
        elif self.capitalisation_key=="end":
                profit = 0
                for i in range(0,self.duration):
                    profit+=self.monthly_profit(30, saldo)
                saldo+=profit
        return saldo
    
class SavingsAccount(Deposit):
    
    def __init__(self, saldo=0, interest=0, duration=0):
        Deposit.__init__(self, saldo, interest, duration)
        self.capitalisation_key="month"
        self.capitalisation=DURATION_ENUM[self.capitalisation_key]
    
    def calculate_for_monthly_income(self, transfers, saldo):
        transfes_overall = 0
        for i in range(0, self.duration):
            saldo += self.monthly_profit(31, saldo)
            if i < transfers.__len__():
                saldo += transfers[i]
                transfes_overall += transfers[i]
        return {"total":saldo, "transfes_overall":transfes_overall}
        
if __name__ == '__main__':
    as = SavingsAccount(saldo=15000,interest=4.1, duration=12)
    transfers= [1500,1500,1500,1500,1500,1500,0,0]
    result = as.calculate_for_monthly_income(transfers, as.saldo)
    #print "income_no_profit= " + str(result["income"])
    #print "income_saldo= " + str(result["income_saldo"])
    print "profit= " + str(result["total"]-as.saldo-result["transfes_overall"])
    print "total= "+str(result["total"])
    
    as = SavingsAccount(saldo=5000,interest=4.1, duration=12)
    transfers= [1500,1500,1500,1500,1500,1500,0,0]
    result = as.calculate_for_monthly_income(transfers, as.saldo)
    #print "income_no_profit= " + str(result["income"])
    #print "income_saldo= " + str(result["income_saldo"])
    print "profit= " + str(result["total"]-as.saldo-result["transfes_overall"])
    print "total= "+str(result["total"])
    #print "average= " +str((result["total"]-as.saldo)/transfers.__len__())
    
    as = SavingsAccount(saldo=10000,interest=5.35, duration=12)
    
    as.capitalisation_key="month"
    as.capitalisation=DURATION_ENUM[as.capitalisation_key]
    result = as.calculate_total_profit(as.saldo)
    print "lokata= "+str(result)
    
    as.capitalisation_key="end"
    as.capitalisation=DURATION_ENUM[as.capitalisation_key]
    result = as.calculate_total_profit(as.saldo)
    print "lokata= "+str(result)