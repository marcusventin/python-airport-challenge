from airport import Airport
from plane import Plane

class TestAirport():
    def test_hangar_is_empty(self):
        airport = Airport()
        assert airport.hangar == []
    
    def test_land_adds_plane_to_hangar(self):
        airport = Airport()
        plane = Plane()
        assert plane not in airport.hangar
        airport.land(plane)
        assert plane in airport.hangar