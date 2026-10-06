import math


class ParkingTicket():
    """Parking ticket for a ticketed car."""

    def __init__(self, car, officer, illegal_minutes):
        """Creates a parking ticket."""

        self.car = car
        self.officer = officer

        if not isinstance(illegal_minutes, int):
            raise TypeError
        elif not (0 < illegal_minutes):
            raise ValueError
        else:
            self._illegal_minutes = illegal_minutes

    @property
    def make(self) -> str:
        """Return the make of the car."""
        return self.car.make

    @property
    def model(self) -> str:
        """Return the model of the car."""
        return self.car.model

    @property
    def color(self) -> str:
        """Return the color of the car."""
        return self.car.color

    @property
    def license_number(self) -> str:
        """Return the license number of the car."""
        return self.car.license_number

    @property
    def illegal_minutes(self) -> int:
        """Return the number of illegal parking minutes."""
        return self._illegal_minutes

    @property
    def fine(self) -> float:
        """Fine based on the number of illegal minutes."""
        hours = math.ceil(self.illegal_minutes / 60)

        if hours == 1:
            return 25
        else:
            return 25 + ((hours - 1) * 10)

    @property
    def officer_name(self) -> str:
        """Return the name of the officer issuing the ticket."""
        return self.officer.name

    @property
    def badge_number(self) -> int:
        """Return the badge number of the officer issuing the ticket."""
        return self.officer.badge_number

    def report(self) -> str:
        """Return a readable parking ticket report."""

        return (
            "Parking Ticket\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Color: {self.color}\n"
            f"License Number: {self.license_number}\n"
            f"Illegal Minutes: {self.illegal_minutes}\n"
            f"Fine: ${self.fine:.2f}\n"
            f"Officer: {self.officer_name}\n"
            f"Badge Number: {self.badge_number}"
        )
