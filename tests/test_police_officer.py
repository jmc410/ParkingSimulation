import unittest
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class UnittestPoliceOfficer(unittest.TestCase):

    def test_no_ticket_when_time_remaining(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            30
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        result = officer.inspect_car(car, meter)

        self.assertIsNone(result)

    def test_no_ticket_when_time_is_exact(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            60
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        result = officer.inspect_car(car, meter)

        self.assertIsNone(result)

    def test_ticket_when_time_is_exceeded(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            61
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        result = officer.inspect_car(car, meter)

        self.assertIsNotNone(result)
        self.assertIsInstance(result, ParkingTicket)

    def test_illegal_minutes(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            90
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        ticket = officer.inspect_car(car, meter)

        self.assertEqual(ticket.illegal_minutes, 30)

    def test_ticket_car_information(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            90
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        ticket = officer.inspect_car(car, meter)

        self.assertEqual(ticket.make, "Toyota")
        self.assertEqual(ticket.model, "Camry")
        self.assertEqual(ticket.color, "Blue")
        self.assertEqual(ticket.license_number, "L1C3NSEPLT")

    def test_ticket_officer_information(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            90
        )

        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        ticket = officer.inspect_car(car, meter)

        self.assertEqual(ticket.officer_name, "MP Barnes")
        self.assertEqual(ticket.badge_number, 1207)

    def test_incorrect_car(self):
        meter = ParkingMeter(60)
        officer = PoliceOfficer("MP Barnes", 1207)

        with self.assertRaises(TypeError):
            officer.inspect_car("not a car", meter)

    def test_incorrect_meter(self):
        car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            60
        )

        officer = PoliceOfficer("MP Barnes", 1207)

        with self.assertRaises(TypeError):
            officer.inspect_car(car, "not a meter")


if __name__ == "__main__":
    unittest.main()

