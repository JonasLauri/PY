import datetime

class Player:
    
    # Class variables
    num_of_players = 0
    raise_amount = 1.03

    # Instance variables
    def __init__(self, name, last, email, scores):
        self.name = name
        self.last = last
        self.email = email
        self.scores = scores
        Player.num_of_players += 1

    # Instance methods
    def info(self):
        return f"{self.name}, {self.last}, {self.email}, {self.scores}"

    def score_raise(self):
        self.scores = int(self.scores * self.raise_amount)

    # Class methods
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    # Additional cls construction
    @classmethod
    def from_string(cls, pl_str):
        first, last, mail, scor = pl_str.split(" ")
        return cls(first, last, mail, scor)

    # Static methods
    @staticmethod
    def is_wday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

player1 = 'Jonas Laurinaitis jonas@gmail.com 50000'
new_user = Player.from_string(player1)
print(new_user.info())

my_date = datetime.date(2020, 5, 31)
print(Player.is_wday(my_date))