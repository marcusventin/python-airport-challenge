from unittest.mock import patch

from weather import Weather

class TestWeather():
    @patch('random.randint')
    def test_returns_true_when_storm(self, mocked_randint):
        odds = Weather.odds
        mocked_randint.return_value = odds
        assert Weather.storm_check() == True
        mocked_randint.assert_called_with(1, odds)
    
    @patch('random.randint')
    def test_returns_false_when_no_storm(self, mocked_randint):
        odds = Weather.odds
        mocked_randint.return_value = odds - 1
        assert Weather.storm_check() == False
        mocked_randint.assert_called_with(1, odds)

        

        

