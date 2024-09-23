from musician import Musician


class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def add_musician(self, musician):
        self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            musician.play()

    def __str__(self):
        return f"band ({self.name})" + ", ".join([str(musician) for musician in self.musicians])
