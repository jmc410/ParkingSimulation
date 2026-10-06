import unittest
from parking_meter import ParkingMeter


class UnittestParkingMeter(unittest.TestCase):

    def test_parkingmeter(self):
        meter = ParkingMeter(60)

        result = meter.minutes_purchased
        self.assertEqual(result, 60)

    def test_zero_minutes(self):
        meter = ParkingMeter(0)

        self.assertEqual(meter.minutes_purchased, 0)

    def test_positive_minutes(self):
        meter = ParkingMeter(120)

        self.assertEqual(meter.minutes_purchased, 120)

    def test_negative_minutes(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-1)

    def test_noninteger_minutes(self):
        with self.assertRaises(TypeError):
            ParkingMeter(60.5)

    def test_property_reassignment(self):
        meter = ParkingMeter(60)

        meter.minutes_purchased = 120

        self.assertEqual(meter.minutes_purchased, 120)

    def test_invalid_property_reassignment(self):
        meter = ParkingMeter(60)

        with self.assertRaises(ValueError):
            meter.minutes_purchased = -10

    def test_incorrect_property_reassignment(self):
        meter = ParkingMeter(60)

        with self.assertRaises(TypeError):
            meter.minutes_purchased = 60.5


if __name__ == "__main__":
    unittest.main()
