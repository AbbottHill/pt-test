

class Player:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def showinfo(self):
        print('%s\'s hp is %s' % (self.name, self.hp))

    def updatename(self, newname):
        self.name = newname


class VipPlayer(Player):
    def __init__(self, name, hp=1000, level=100):
        super().__init__(name, hp)
        self.level = level


tom = Player('Tom', 100)
tom.showinfo()

cd = VipPlayer('cd')
cd.showinfo()

