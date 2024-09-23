import random
from tree import Tree

class FruitTree(Tree):
    def __init__(self, height, leaves):
        super().__init__(height, leaves)
        self.fruit = 1  # Initialize with 1 fruit

    def grow(self):
        super().grow()  # Call the base class grow method

        # Chance to gain a fruit (1 in 2)
        if random.randint(1, 2) == 1:
            self.fruit += 1

        # Chance to lose a fruit (1 in 5)
        if random.randint(1, 5) == 1 and self.fruit > 0:
            self.fruit -= 1

    def __str__(self):
        return f"FruitTree(height={self.height}, leaves={self.leaves}, fruit={self.fruit})"
