from unittest.mock import patch
import pytest
from airport import Airport
from plane import Plane
from weather import Weather

class TestAirport():
    def test_hangar_is_empty(self):
        airport = Airport()
        assert airport.hangar == []

    @patch.object(Weather, 'storm_check')
    def test_land_adds_plane_to_hangar(self, mocked_weather_check):
        mocked_weather_check.return_value = False
        airport = Airport()
        plane = Plane()
        assert plane not in airport.hangar
        airport.land(plane)
        assert plane in airport.hangar
    
    @patch.object(Weather, 'storm_check')
    def test_launch_removes_plane_from_hangar(self, mocked_weather_check):
        mocked_weather_check.return_value = False
        airport = Airport()
        plane = Plane()
        plane.airborne = False
        airport.hangar = [plane]
        airport.launch(plane)
        assert plane not in airport.hangar
    
    @patch.object(Weather, 'storm_check')
    def test_land_raises_error_when_hangar_full(self, mocked_weather_check):
        mocked_weather_check.return_value = False
        with pytest.raises(Exception, 
            match="There's no space in this hangar!"):
            airport = Airport()
            airport.hangar = [Plane() for num in range(airport.capacity)]
            plane = Plane()
            airport.land(plane)
    
    def test_custom_default_capacity(self):
        airport1 = Airport(3)
        assert airport1.capacity == 3

        airport2 = Airport(17)
        assert airport2.capacity == 17
    
    @patch.object(Weather, 'storm_check')
    def test_launch_raises_error_when_stormy(self, mocked_weather_check):
        mocked_weather_check.return_value = True
        with pytest.raises(Exception,
            match="It's too stormy to launch!"):
            airport = Airport()
            plane = Plane()
            plane.airborne = False
            airport.hangar = [plane]
            airport.launch(plane)
    
    @patch.object(Weather, 'storm_check')
    def test_land_raises_error_if_stormy(self, mocked_weather_check):
        mocked_weather_check.return_value = True
        with pytest.raises(Exception,
            match="It's too stormy to land!"):
            airport = Airport()
            plane = Plane()
            airport.land(plane)
        
