class Airport():
    def __init__(self):
        self.hangar = []

    def land(self, plane):
        plane.land(self)