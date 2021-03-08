import pickle
from positions import QB, HB, WR, TE, K

class Draft:
    def __init__(self):
        self.teams = 10
        self.ordering = ['QB', 'HB', 'HB', 'WR', 'WR', 'TE', 'FLEX', 'DEF', 'K', 'QB', 'HB', 'WR', 'TE', 'FLEX']
        self.total_rounds = len(self.ordering)
        with open('../data/players.pkl', 'rb') as inp:
            self.players = pickle.load(inp)
        self.sortByOvr(self.players)
        for i in self.players:
            print(i.attributes)
            #if isinstance(i, QB):
                #print(i.attributes)

    """
    Return 2D list of players you will select from depending on the round.
    Need to make if statements for each round as they are unique.
    Figure out how to get top ten of a certain position of players (assume players are sorted)
    and remove them from the overall pool of players (self.players)
    Note: Can determine position of object via isinstance(object, class)  (returns boolean)
    Ex: if isinstance(self.players[i], QB)
    Base Structure provided (keep it)
    
    """
    def generateRoundPools(self):
        all_round_pools = []
        round_count = 1
        while round_count <= self.total_rounds:
            round_pool = []



            all_round_pools.append(round_pool)
            round_count += 1

        return all_round_pools

    """
    Performs merge sort on players' overalls.
    Note: All parameters in python are passed by reference (not const)
    """
    def sortByOvr(self, lst):
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]
            self.sortByOvr(left)
            self.sortByOvr(right)

            # Merge into sorted list
            # i => left index, j => right index
            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
                if left[i].getOverall() <= right[j].getOverall():
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1


if __name__ == '__main__':
    d = Draft()
