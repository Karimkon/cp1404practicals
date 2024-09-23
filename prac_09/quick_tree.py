from tree import Tree

class QuickTree(Tree):
    def grow(self, sunlight, water):
        self.leaves += sunlight
        self.height += water

    def __str__(self):
        return f"QuickTree(height={self.height}, leaves={self.leaves})"
