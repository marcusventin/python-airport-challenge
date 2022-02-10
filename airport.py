class Airport():
    def __init__(self):
        self.hangar = []
        self.capacity = 5

    def land(self, plane):
        if len(self.hangar) >= self.capacity:
            raise OverflowError("There's no space in this hangar!")
        else:
            plane.land(self)
    
    def launch(self, plane):
        plane.take_off(self)