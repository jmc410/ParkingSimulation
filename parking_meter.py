
class ParkingMeter():
    """Bought parking time."""

    def __init__(self, minutes_purchased):

        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self) -> int:
        """Return the number of purchased parking minutes."""
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, minutes: int):
        """Set the number of purchased parking minutes."""
        if not isinstance(minutes, int):
            raise TypeError
        elif not (0 <= minutes):
            raise ValueError
        else:
            self._minutes_purchased = minutes
