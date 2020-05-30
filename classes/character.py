class Player:
    
    num_of_players = 0
    raise_amount = 2

    def __init__(self, name, last, email, scores):
        self.name = name
        self.last = last
        self.email = email
        self.scores = scores
        Player.num_of_players += 1

    def info(self):
        return f"{self.name}, {self.last}, {self.email}, {self.scores}"

    def score_raise(self):
        self.scores = int(self.scores * self.raise_amount)
    

