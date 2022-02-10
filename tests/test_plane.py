from plane import Plane
from airport import Airport

class TestPlane():
    def test_ground_changes_airborne_to_false(self):
        plane = Plane()
        assert plane.airborne == True
        plane.ground()
        assert plane.airborne == False

    def test_land_adds_to_airport_hangar(self):
        airport = Airport()
        plane = Plane()
        plane.land(airport)
        assert plane in airport.hangar

    def test_fly_changes_airborne_to_true(self):
        plane = Plane()
        plane.airborne = False
        plane.fly()
        assert plane.airborne == True
    
    def test_take_off_removes_from_airport_hangar(self):
        airport = Airport()
        plane = Plane()
        airport.hangar = [plane]
        plane.take_off(airport)
        assert plane not in airport.hangar
