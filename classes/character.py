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
        self.scores = int(scores)
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
    
    # Built-in methods
    def __add__(self, other):
        return self.scores + other.scores

#my_date = datetime.date(2020, 5, 31)
#print(Player.is_wday(my_date))

class Dev(Player):
    raise_amount = 2.3
    def __init__(self, name, last, email, scores, lang):
        super().__init__(name, last, email, scores)
        self.lang = lang

#user = Dev("Jonas", "Laurinaitis", "jonas@gmail.com", 50000, "java")
#print(user.lang)

class Mangr(Player):

    def __init__(self, name, last, email, scores, players=None):
        super().__init__(name, last, email, scores)
        if players is None:
            self.players = []
        else:
            self.players = players
    
    def add_pl(self, playr):
        if playr not in self.players:
            self.players.append(playr)
    
    def remove_pl(self, playr):
        if playr in self.players:
            self.players.remove(playr)
        
    def print_pls(self):
        for pl in self.players:
            print(pl.info())

dev_1 = Dev("Tom", "Tom", "tom@gmail.com", 50000, "golang")
dev_2 = Dev("Rob", "Rob", "rob@gmail.com", 1000, "abc")

boss = Mangr("bob", "bobinski", "bob@gmail.com", 100000, [dev_1, dev_2])

print(boss.info())
boss.print_pls()