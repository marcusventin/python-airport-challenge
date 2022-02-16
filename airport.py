from weather import Weather

class Airport():
    DEFAULT_CAPACITY = 8

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.hangar = []
        self.capacity = capacity

    def land(self, plane):
        if self.weather_check() == True:
            raise Exception("It's too stormy to land!")
        if len(self.hangar) >= self.capacity:
            raise Exception("There's no space in this hangar!")
        else:
            plane.land(self)
    
    def launch(self, plane):
        if self.weather_check() == True:
            raise Exception("It's too stormy to launch!")
        plane.take_off(self)

    def weather_check(self):
        return(Weather.storm_check())