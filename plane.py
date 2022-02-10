
class Plane():
    def __init__(self):
        self.airborne = True
    
    def land(self, airport):
        airport.hangar.append(self)
        self.ground()
    
    def ground(self):
        self.airborne = False