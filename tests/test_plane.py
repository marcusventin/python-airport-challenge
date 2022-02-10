from plane import Plane
from airport import Airport

class TestPlane():
    def test_ground_changes_status_to_grounded(self):
        plane = Plane()
        assert plane.airborne == True
        plane.ground()
        assert plane.airborne == False

    def test_land_adds_to_airport_hangar(self):
        airport = Airport()
        plane = Plane()
        plane.land(airport)
        assert plane in airport.hangar

