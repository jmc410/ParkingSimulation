
class ParkedCar():
    def __init__ (self, make, model, color, license_number, minutes_parked):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def minutes_parked(self) -> int:
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes: int):
        if not isinstance(minutes, int):
            raise TypeError
        elif not (0 <= minutes):
            raise ValueError
        else:
            self._minutes_parked = minutes

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, make: str):
        if not isinstance(make, str):
            raise TypeError
        elif not make or not make.strip():
            raise ValueError
        else:
            self._make = make

    

    