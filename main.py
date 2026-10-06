"""Parking ticket simulator."""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    """Runs the parking ticket simulator."""
    car = ParkedCar("Toyota", "Camry", "Blue", "L1C3NSEPLT", 75)
    meter = ParkingMeter(60)
    officer = PoliceOfficer("MP Barnes", 1207)

    ticket = officer.inspect_car(car, meter)

    if ticket is None:
        print("No parking violation issued.")
    else:
        print(ticket.report())


if __name__ == "__main__":
    main()
