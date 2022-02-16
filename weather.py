import random

class Weather():
    odds = 60
    
    @classmethod
    def storm_check(cls):
        number = random.randint(1, Weather.odds)
        return(number == Weather.odds)
