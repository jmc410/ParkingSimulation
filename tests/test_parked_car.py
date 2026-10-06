import unittest
from parked_car import ParkedCar



class UnittestParkedCar(unittest.TestCase):

    def test_parkedcar(self):
        car = ParkedCar("Toyota","Camry","Blue","L1C3NSEPLT",60)

        result = car.make
        self.assertEqual(result,"Toyota")

        result = car.model
        self.assertEqual(result, "Camry")

        result = car.color
        self.assertEqual(result, "Blue")

        result = car.license_number
        self.assertEqual(result, "L1C3NSEPLT")

        result = car.minutes_parked
        self.assertEqual(result, 60)


def test_property_reassignment(self):
        car = ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", 60)

        car.make = "Honda"
        car.model = "Civic"
        car.color = "Red"
        car.license_number = "ABC123"
        car.minutes_parked = 30

        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.color, "Red")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 30)

    def test_empty_make(self):
        with self.assertRaises(ValueError):
            ParkedCar("", "Camry", "Blue", "L1C3NSEPLT", 60)

    def test_incorrect_make(self):
        with self.assertRaises(TypeError):
            ParkedCar(123, "Camry", "Blue", "L1C3NSEPLT", 60)

    def test_empty_model(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "", "Blue", "L1C3NSEPLT", 60)

    def test_incorrect_model(self):
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", 123, "Blue", "L1C3NSEPLT", 60)

    def test_empty_color(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "", "L1C3NSEPLT", 60)

    def test_incorrect_color(self):
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", 123, "L1C3NSEPLT", 60)

    def test_empty_license_number(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "", 60)

    def test_incorrect_license_number(self):
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", 123, 60)

    def test_zero_minutes(self):
        car = ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", 0)

        self.assertEqual(car.minutes_parked, 0)

    def test_positive_minutes(self):
        car = ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", 60)

        self.assertEqual(car.minutes_parked, 60)

    def test_negative_minutes(self):
        with self.assertRaises(ValueError):
            ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", -1)

    def test_noninteger_minutes(self):
        with self.assertRaises(TypeError):
            ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", 60.5)


if __name__ == "__main__":
    unittest.main()