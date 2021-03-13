import pickle
from positions import QB, HB, WR, TE, K
import random

class Draft:
    def __init__(self):
        self.teams = 10
        self.ordering = ['QB', 'HB', 'HB', 'WR', 'WR', 'TE', 'FLEX', 'DEF', 'K', 'QB', 'HB', 'WR', 'TE', 'FLEX']
        self.total_rounds = len(self.ordering)
        with open('../data/players.pkl', 'rb') as inp:
            self.players = pickle.load(inp)
        self.sortByOvr(self.players)
        

    """
    Return 2D list of players you will select from depending on the round.
    Need to make if statements for each round as they are unique.
    Use def getTopPlayers().
    Note: Can determine position of object via isinstance(object, class)  (returns boolean)
    Ex: if isinstance(self.players[i], QB)
    Base Structure provided (keep it)
    
    """
    def generateRoundPools(self):
        all_round_pools = []
        round_count = 1
        self.defenses = ['Arizona Cardinals D/ST', 'Atlanta Falcons D/ST', 'Baltimore Ravens D/ST', 
                    'Buffalo Bills D/ST', 'Carolina Panthers D/ST', 'Chicago Bears D/ST', 
                    'Cincinnati Bengals D/ST', 'Cleveland Browns D/ST', 'Dallas Cowboys D/ST', 
                    'Denver Broncos D/ST', 'Detroit Lions D/ST', 'Green Bay Packers D/ST', 
                    'Houston Texans D/ST', 'Indianapolis Colts D/ST', 'Jacksonville Jaguars D/ST',
                    'Kansas City Chiefs D/ST', 'Oakland Raiders D/ST', 'Los Angeles Chargers D/ST',
                    'Los Angeles Rams D/ST', 'Miami Dolphins D/ST', 'Minnesota Vikings D/ST', 
                    'New England Patriots D/ST', 'New Orleans Saints D/ST', 'New York Giants D/ST',
                    'New York Jets D/ST', 'Philadelphia Eagles D/ST', 'Pittsburgh Steelers D/ST',
                    'San Francisco 49ers D/ST', 'Seattle Seahwaks D/ST', 'Tampa Bay Buccaneers D/ST',
                    'Tennessee Titans D/ST', 'Washington Football Team D/ST']
        while round_count <= self.total_rounds:
            round_pool = []
            if round_count == 1 or round_count == 9 :
                round_pool = self.getTopPlayers('QB')
            elif round_count == 2 or round_count == 3 or round_count == 10 :
                round_pool = self.getTopPlayers('HB')
            elif round_count == 4 or round_count == 5 or round_count == 11 :
                round_pool = self.getTopPlayers('WR')
            elif round_count == 6 or round_count == 12 :
                round_pool = self.getTopPlayers('TE')
            elif round_count == 7 or round_count == 13:
                round_pool = self.getTopPlayers('FLEX')
            elif round_count == 8 :
                round_pool = self.getTopPlayers('K')
            elif round_count == 10 :
                round_pool = self.getTopPlayers('FLEX')
            elif round_count == 14 :
                randDefense = random.choice(self.defenses)
                self.defenses.remove(randDefense)
                #Add randDefense to the team's roster
                
            all_round_pools.append(round_pool)
            round_count += 1

        return all_round_pools

    """
    Get top N players from self.players (N = self.teams). Remove these players from total player pool (self.players)
    4 different key params: 'QB', 'HB', 'WR', 'TE', 'K', 'FLEX'
    Assume list is sorted.
    """
    def getTopPlayers(self, key='QB'):
        returnlist = []
        selections = 0
        for i in range(len(self.players)-1, -1, -1):
            if self.players[i].getPosition() == str.upper(key) :
                if selections < 10:
                    selections+=1
                    returnlist.append(self.players[i])
                    self.players.remove(self.players[i])
                else:
                    break
            if str.upper(key) == 'FLEX' :
                if self.players[i].getPosition() == 'HB' or self.players[i].getPosition() == 'WR' or self.players[i].getPosition() == 'TE' :
                    if selections < 10:
                        selections+=1
                        returnlist.append(self.players[i])
                        self.players.remove(self.players[i])
                    else:
                        break
        random.shuffle(returnlist)
        return returnlist

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

