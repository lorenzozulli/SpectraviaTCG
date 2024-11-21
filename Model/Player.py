import random

class Player(object):
    def __init__(self, name):
        self.name = name

    def randomizeName():
        number = random.randint(1111, 9999)
        player = "Player_" + str(number)
        return player
