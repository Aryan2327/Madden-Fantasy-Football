import pickle
class Draft:
    def __init__(self):
        self.teams = 10
        self.ordering = ['QB', 'HB', 'HB', 'WR', 'WR', 'TE', 'FLEX', 'DEF', 'K', 'QB', 'HB', 'WR', 'TE', 'FLEX']
        self.rounds = len(self.ordering)
        self.round_counter = 1
        with open('../data/players.pkl', 'rb') as inp:
            self.players = pickle.load(inp)

    """
    Return list of players you will select from depending on the round.
    """
    def roundPool(self):
        if self.round_counter == 1:
            pass

        self.round_counter += 1
        return []
