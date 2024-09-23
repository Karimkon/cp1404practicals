class Tree:
    def __init__(self, height, leaves):
        self.height = height
        self.leaves = leaves

    def grow(self):
        self.height += 1
        self.leaves += 1

    def __str__(self):
        return f"Tree(height={self.height}, leaves={self.leaves})"
