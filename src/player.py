from collections import OrderedDict


class Player(object):
    """
    Param(attributes): Takes an OrderedDict of all of the player's stats
    """

    def __init__(self, attributes):
        self.attributes = attributes

    """
    Displays all specific values and stats for player in a pretty format
    """
    def show(self):
        print("Name:", self.attributes["Name"], "\nPosition:", self.attributes["Position"], "\nTeam:", self.attributes["Team"], "\nAge:", str(self.attributes["Age"]), "\nHealth Rating:", str(self.attributes["Health Rating"]), "\nOverall:", str(self.attributes["Overall"]), "\n")
        