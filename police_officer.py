from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket


class PoliceOfficer():
    """Police officer that can inspect parked cars."""

    def __init__(self, name, badge_number):
        self.name = name
        self.badge_number = badge_number

    @property
    def name(self) -> str:
        """Return the officer's name."""
        return self._name

    @name.setter
    def name(self, name: str):
        """Set the officer's name."""
        if not isinstance(name, str):
            raise TypeError
        elif not name or not name.strip():
            raise ValueError
        else:
            self._name = name

    @property
    def badge_number(self) -> int:
        """Return the officer's badge number."""
        return self._badge_number

    @badge_number.setter
    def badge_number(self, badge_number: int):
        """Set the officer's badge number."""
        if not isinstance(badge_number, int):
            raise TypeError
        elif not (0 <= badge_number):
            raise ValueError
        else:
            self._badge_number = badge_number

    def inspect_car(self, car, meter):
        if not isinstance(car, ParkedCar):
            raise TypeError

        if not isinstance(meter, ParkingMeter):
            raise TypeError

        if car.minutes_parked <= meter.minutes_purchased:
            return None
        else:
            illegal_minutes = car.minutes_parked - meter.minutes_purchased
            return ParkingTicket(car, self, illegal_minutes)
