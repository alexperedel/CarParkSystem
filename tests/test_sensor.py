import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(id=1, car_park=self.car_park)
        self.exit_sensor = ExitSensor(id=2, car_park=self.car_park)

    def test_entry_sensor_initialization(self):
        self.assertIsInstance(self.entry_sensor, EntrySensor)
        self.assertFalse(self.entry_sensor.is_active)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertIsInstance(self.entry_sensor.car_park, CarPark)

    def test_exit_sensor_initialization(self):
        self.assertIsInstance(self.exit_sensor, ExitSensor)
        self.assertFalse(self.exit_sensor.is_active)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertIsInstance(self.exit_sensor.car_park, CarPark)

    def test_entry_sensor_detect_vehicle(self):
        plate_count = len(self.entry_sensor.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.entry_sensor.car_park.plates), plate_count + 1)

    def test_exit_sensor_detect_vehicle(self):
        self.exit_sensor.car_park.plates.append("FAKE-72303d")
        plate_count = len(self.exit_sensor.car_park.plates)
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.exit_sensor.car_park.plates), plate_count - 1)




