from random import randint

class Die:
    # Init dtheie characteristics
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be int")
        self.value = value or randint(1, sides)

    def __int__(self):
        return self.value

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self)  != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __len__(self):
        return int(self)

    def __repr__(self):
        return str(self.value)


class D6(Die):
    # Die subclassing for 6 sided die
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
