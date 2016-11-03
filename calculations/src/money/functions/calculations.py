from Lib import logging
import datetime
from datetime import date

from calculations.src.money.functions.insterests import Interests

if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger = logging.getLogger('calculations')
    logger.setLevel(logging.INFO)
    logger.addHandler(console)
    logger.info('Hello')

    interests = Interests()

    interests.interstAmount = 1
    interests.interestDuration = 12
    interests.interestCalculationType = 'daily'

    incomes = dict()
    incomes[datetime.date(2016, 1, 1)] = 100
    incomes[datetime.date(2016, 1, 2)] = 200
    incomes[datetime.date(2016, 1, 3)] = 200

    for income_date in incomes.keys():
        logger.info(income_date.isoformat())

