
class ParkedCar():
    def __init__ (self, make, model, color, license_number, minutes_parked):
        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def minutes_parked(self) -> int:
        """Returns the number of minutes parked."""
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, minutes: int):
        """Sets the number of minutes parked."""
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

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, model: str):
        if not isinstance(model, str):
            raise TypeError
        elif not model or not model.strip():
            raise ValueError
        else:
            self._model = model
    

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, color: str):
        if not isinstance(color, str):
            raise TypeError
        elif not color or not color.strip():
            raise ValueError
        else:
            self._color = color

    @property
    def license_number(self) -> str:
        return self._license_number

    @license_number.setter
    def license_number(self, license_number: str):
        if not isinstance(license_number, str):
            raise TypeError
        elif not license_number or not license_number.strip():
            raise ValueError
        else:
            self._license_number = license_number



    