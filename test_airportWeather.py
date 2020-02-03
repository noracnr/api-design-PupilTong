from airportWeather import *
import pytest
def test_airportInfo():
    assert airportWeather("BOS").GetAirportInfo() == """{"iata_code": "BOS", "id": "3422", "ident": "KBOS", "type": "large_airport", "name": "General Edward Lawrence Logan International Airport", "locate": {"latitude_deg": "42.36429977", "longitude_deg": "-71.00520325", "elevation_ft": "20", "continent": "NA", "iso_country": "US", "iso_region": "US-MA", "municipality": "Boston"}, "scheduled_service": "yes", "gps_code": "KBOS", "local_code": "BOS", "internet_info": {"home_link": "http://www.massport.com/logan/", "wikipedia_link": "https://en.wikipedia.org/wiki/Logan_International_Airport", "keywords": ["General", "Edward", "Lawrence", "Logan", "International", "Airport"]}}"""
    with pytest.raises(Exception):
        assert(airportWeather("PKX"))
        assert(airportWeather(""))
    