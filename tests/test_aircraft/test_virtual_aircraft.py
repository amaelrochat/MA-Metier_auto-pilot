import pytest
from unittest.mock import patch
from src.models.aircrafts.virtual_aircraft import VirtualAircraft


@pytest.fixture
def mock_simconnect():
    with patch('src.models.aircrafts.virtual_aircraft.SimConnect') as mock:
        yield mock.return_value


@pytest.fixture
def mock_aircraft_requests():
    with patch('src.models.aircrafts.virtual_aircraft.AircraftRequests') as mock:
        yield mock.return_value


@pytest.fixture
def virtual_aircraft(mock_simconnect, mock_aircraft_requests):
    return VirtualAircraft()


class TestVirtualAircraftProperties:
    def test_altitude(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 10000.0
        assert virtual_aircraft.altitude == 10000.0
        mock_aircraft_requests.get.assert_called_with("PLANE_ALTITUDE")

    def test_ground_altitude(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 500.0
        assert virtual_aircraft.ground_altitude == 500.0
        mock_aircraft_requests.get.assert_called_with("GROUND_ALTITUDE")

    def test_ground_speed(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 140.0
        assert virtual_aircraft.ground_speed == 140.0
        mock_aircraft_requests.get.assert_called_with("GROUND_VELOCITY")

    def test_speed(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 150.0
        assert virtual_aircraft.speed == 150.0
        mock_aircraft_requests.get.assert_called_with("AIRSPEED_INDICATED")

    def test_heading(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 270.0
        assert virtual_aircraft.heading == 270.0
        mock_aircraft_requests.get.assert_called_with(
            "MAGNETIC_COMPASS")

    def test_latitude(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 37.7749
        assert virtual_aircraft.latitude == 37.7749
        mock_aircraft_requests.get.assert_called_with("PLANE_LATITUDE")

    def test_longitude(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = -122.4194
        assert virtual_aircraft.longitude == -122.4194
        mock_aircraft_requests.get.assert_called_with("PLANE_LONGITUDE")

    def test_plane_angle(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 5.0
        assert virtual_aircraft.plane_angle == 5.0
        mock_aircraft_requests.get.assert_called_with("PLANE_BANK_DEGREES")


class TestVirtualAircraftSetters:
    def test_throttle_getter(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 0.75
        assert virtual_aircraft.throttle == 0.75
        mock_aircraft_requests.get.assert_called_with(
            "GENERAL_ENG_THROTTLE_LEVER_POSITION:1")

    def test_throttle_setter(self, virtual_aircraft, mock_aircraft_requests):
        virtual_aircraft.throttle = 0.8
        mock_aircraft_requests.set.assert_called_with(
            "GENERAL_ENG_THROTTLE_LEVER_POSITION:1", 0.8)

    def test_aileron_position_getter(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 0.1
        assert virtual_aircraft.aileron_position == 0.1
        mock_aircraft_requests.get.assert_called_with("AILERON_POSITION")

    def test_aileron_position_setter(self, virtual_aircraft, mock_aircraft_requests):
        virtual_aircraft.aileron_position = 0.15
        mock_aircraft_requests.set.assert_called_with("AILERON_POSITION", 0.15)

    def test_rudder_position_getter(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = -0.05
        assert virtual_aircraft.rudder_position == -0.05
        mock_aircraft_requests.get.assert_called_with("RUDDER_POSITION")

    def test_rudder_position_setter(self, virtual_aircraft, mock_aircraft_requests):
        virtual_aircraft.rudder_position = 0.2
        mock_aircraft_requests.set.assert_called_with("RUDDER_POSITION", 0.2)

    def test_elevator_position_getter(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 0.0
        assert virtual_aircraft.elevator_position == 0.0
        mock_aircraft_requests.get.assert_called_with("ELEVATOR_POSITION")

    def test_elevator_position_setter(self, virtual_aircraft, mock_aircraft_requests):
        virtual_aircraft.elevator_position = -0.1
        mock_aircraft_requests.set.assert_called_with(
            "ELEVATOR_POSITION", -0.1)

    def test_spoiler_position_getter(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.return_value = 0.0
        assert virtual_aircraft.spoiler_position == 0.0
        mock_aircraft_requests.get.assert_called_with(
            "SPOILERS_HANDLE_POSITION")

    def test_spoiler_position_setter(self, virtual_aircraft, mock_aircraft_requests):
        virtual_aircraft.spoiler_position = 0.5
        mock_aircraft_requests.set.assert_called_with(
            "SPOILERS_HANDLE_POSITION", 0.5)

    def test_to_array(self, virtual_aircraft, mock_aircraft_requests):
        mock_aircraft_requests.get.side_effect = [
            10000.0, 0.0, 0.0, 500.0, 130.0, 150.0, 270.0,
            0.75, 0.1, -0.05, 0.0, 0.0, 0.0
        ]
        result = virtual_aircraft.to_array()
        assert result == {
            "altitude": 10000.0,
            "latitude": 0.0,
            "longitude": 0.0,
            "ground_altitude": 500.0,
            "ground_speed": 130.0,
            "speed": 150.0,
            "heading": 270.0,
            "throttle": 0.75,
            "aileron_position": 0.1,
            "rudder_position": -0.05,
            "elevator_position": 0.0,
            "spoiler_position": 0.0,
            "plane_angle": 0.0
        }
