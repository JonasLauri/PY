class GameScores:
    # Return the highest game score when specific size of even dice is set
    def _score_set(self, hand, set_size):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth*set_size)
        
        return max(scores)

    # Setting score of 2 even dice
    def score_one_pair(self, hand):
        return self._score_set(hand, 2)