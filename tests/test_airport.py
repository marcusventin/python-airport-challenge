import pytest

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
    
    def test_launch_removes_plane_from_hangar(self):
        airport = Airport()
        plane = Plane()
        airport.hangar = [plane]
        airport.launch(plane)
        assert plane not in airport.hangar
    
    def test_land_raises_error_when_hangar_full(self):
        with pytest.raises(OverflowError, 
            match="There's no space in this hangar"):
            airport = Airport()
            airport.hangar = [Plane() for num in range(airport.capacity)]
            plane = Plane()
            airport.land(plane)
    
    def test_custom_default_capacity(self):
        airport1 = Airport(3)
        assert airport1.capacity == 3

        airport2 = Airport(17)
        assert airport2.capacity == 17
