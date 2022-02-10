class Airport():
    def __init__(self):
        self.hangar = []

    def land(self, plane):
        plane.land(self)
    
    def launch(self, plane):
        plane.take_off(self)