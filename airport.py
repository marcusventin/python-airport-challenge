from weather import Weather

class Airport():
    DEFAULT_CAPACITY = 8

    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.hangar = []
        self.capacity = capacity

    def land(self, plane):
        if plane in self.hangar:
            raise Exception("This plane is already in this airport!")
        if plane.airborne == False:
            raise Exception("Your plane is in another airport!")
        if self.weather_check() == True:
            raise Exception("It's too stormy to land!")
        if len(self.hangar) >= self.capacity:
            raise Exception("There's no space in this hangar!")
        else:
            plane.land(self)
    
    def launch(self, plane):
        if plane not in self.hangar:
            raise Exception("Your plane is in another airport!")
        if plane.airborne:
            raise Exception("This plane has already taken off!")
        if self.weather_check() == True:
            raise Exception("It's too stormy to launch!")
        plane.take_off(self)

    def weather_check(self):
        return(Weather.storm_check())