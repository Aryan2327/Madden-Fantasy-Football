import pickle


class Draft:
    def __init__(self):
        self.teams = 10
        self.ordering = ['QB', 'HB', 'HB', 'WR', 'WR', 'TE', 'FLEX', 'DEF', 'K', 'QB', 'HB', 'WR', 'TE', 'FLEX']
        self.rounds = len(self.ordering)
        self.round_counter = 1
        with open('../data/players.pkl', 'rb') as inp:
            self.players = pickle.load(inp)
        self.sortByOvr(self.players)
        for i in self.players:
            print(i.attributes)

    """
    Return list of players you will select from depending on the round.
    """

    def roundPool(self):
        if self.round_counter == 1:
            pass

        self.round_counter += 1
        return []

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
