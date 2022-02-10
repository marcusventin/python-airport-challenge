class Airport():
    DEFAULT_CAPACITY = 8
    def __init__(self, capacity=DEFAULT_CAPACITY):
        self.hangar = []
        self.capacity = capacity

    def land(self, plane):
        if len(self.hangar) >= self.capacity:
            raise OverflowError("There's no space in this hangar!")
        else:
            plane.land(self)
    
    def launch(self, plane):
        plane.take_off(self)