import unittest
from parked_car import ParkedCar
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class UnittestParkingTicket(unittest.TestCase):

    def setUp(self):
        self.car = ParkedCar(
            "Toyota",
            "Camry",
            "Blue",
            "L1C3NSEPLT",
            61
        )

        self.officer = PoliceOfficer("MP Barnes", 1207)

    def test_ticket_information(self):
        ticket = ParkingTicket(self.car, self.officer, 1)

        self.assertEqual(ticket.make, "Toyota")
        self.assertEqual(ticket.model, "Camry")
        self.assertEqual(ticket.color, "Blue")
        self.assertEqual(ticket.license_number, "L1C3NSEPLT")
        self.assertEqual(ticket.officer_name, "MP Barnes")
        self.assertEqual(ticket.badge_number, 1207)

    def test_illegal_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 30)

        self.assertEqual(ticket.illegal_minutes, 30)

    def test_fine_1_minute(self):
        ticket = ParkingTicket(self.car, self.officer, 1)

        self.assertEqual(ticket.fine, 25)

    def test_fine_60_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 60)

        self.assertEqual(ticket.fine, 25)

    def test_fine_61_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 61)

        self.assertEqual(ticket.fine, 35)

    def test_fine_120_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 120)

        self.assertEqual(ticket.fine, 35)

    def test_fine_121_minutes(self):
        ticket = ParkingTicket(self.car, self.officer, 121)

        self.assertEqual(ticket.fine, 45)

    def test_report(self):
        ticket = ParkingTicket(self.car, self.officer, 61)

        result = ticket.report()

        self.assertIn("Toyota", result)
        self.assertIn("Camry", result)
        self.assertIn("Blue", result)
        self.assertIn("L1C3NSEPLT", result)
        self.assertIn("61", result)
        self.assertIn("$35.00", result)
        self.assertIn("MP Barnes", result)
        self.assertIn("1207", result)

    def test_negative_illegal_minutes(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, -1)

    def test_zero_illegal_minutes(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)

    def test_noninteger_illegal_minutes(self):
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, 1.5)


if __name__ == "__main__":
    unittest.main()
