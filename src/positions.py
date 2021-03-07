from player import Player


class QB(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")


class WR(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")


class HB(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")


class TE(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")


class K(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
