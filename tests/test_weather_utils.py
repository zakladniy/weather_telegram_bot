import pytest

from src.application.weather_utils import (
    get_raw_weather_data,
    timestamp_to_iso_date,
    timestamp_to_hour,
    kelvin_to_celsius,
    create_weather_message,
)


def test_get_raw_weather_data() -> None:
    """Test getting raw weather data from Weather API."""
    raw_data = get_raw_weather_data()
    assert isinstance(raw_data, dict)


@pytest.mark.parametrize(
    "test_input,expected", [(1647027129, "01:32:09"), (1657027129, "19:18:49")]
)
def test_timestamp_to_hour(test_input: int, expected: str) -> None:
    """Test converting timestamp to hour string.

    @param test_input: input test timestamp
    @param expected: expected hour string
    """
    assert timestamp_to_hour(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected", [
        (1647027129, "2022-03-12"),
        (1657027129, "2022-07-05")
    ]
)
def test_timestamp_to_iso_date(test_input: int, expected: str) -> None:
    """Test converting timestamp to date in ISO format.

    @param test_input: input test timestamp
    @param expected: expected date in ISO format
    """
    assert timestamp_to_iso_date(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(300, 27), (273, 0)])
def test_kelvin_to_celsius(test_input, expected) -> None:
    """Test converting temperature from kelvin to Celsius.

    @param test_input: input test temperature in kelvin
    @param expected: expected temperature in Celsius
    """
    assert kelvin_to_celsius(test_input) == expected


def test_create_weather_message() -> None:
    """Test correct string with current message weather"""
    assert "Current date" in create_weather_message()
    assert "Weather type" in create_weather_message()
    assert "Weather description" in create_weather_message()
    assert "Current temperature" in create_weather_message()
    assert "Temperature feels like" in create_weather_message()
    assert "Minimum temperature" in create_weather_message()
    assert "Maximum temperature" in create_weather_message()
    assert "Pressure" in create_weather_message()
    assert "Humidity" in create_weather_message()
    assert "Wind speed" in create_weather_message()
    assert "Wind direction" in create_weather_message()
    assert "Sunrise hour" in create_weather_message()
    assert "Sunset hour" in create_weather_message()
