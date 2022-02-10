
class Plane():
    def __init__(self):
        self.airborne = True
    
    def land(self, airport):
        airport.hangar.append(self)
        self.ground()
    
    def take_off(self, airport):
        airport.hangar.remove(self)
        self.fly()
    
    def ground(self):
        self.airborne = False
    
    def fly(self):
        self.airborne = True