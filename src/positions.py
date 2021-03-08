from player import Player


class QB(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
    def getPosition(self):
        return self.attributes.get("Position")


class WR(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
    def getPosition(self):
        return self.attributes.get("Position")


class HB(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
    def getPosition(self):
        return self.attributes.get("Position")


class TE(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
    def getPosition(self):
        return self.attributes.get("Position")


class K(Player):
    def __init__(self, attributes):
        super().__init__(attributes)

    def getOverall(self):
        return self.attributes.get("Overall")
    def getPosition(self):
        return self.attributes.get("Position")