from quick_tree import QuickTree
from fruit_tree import FruitTree

def draw_tree(tree):
    print("Height:", tree.height)
    print("Leaves:", tree.leaves)
    print("Fruit: " + '.' * tree.fruit)

def main():
    # Create instances of QuickTree and FruitTree
    quick_tree = QuickTree(height=5, leaves=10)
    fruit_tree = FruitTree(height=5, leaves=10)

    # Grow the trees
    print("Before growing:")
    print(quick_tree)
    print(fruit_tree)

    # QuickTree grows based on sunlight and water
    quick_tree.grow(sunlight=3, water=2)

    # FruitTree grows, gaining or losing fruit
    fruit_tree.grow()

    print("\nAfter growing:")
    print(quick_tree)
    print(fruit_tree)

    # Visualize the FruitTree
    draw_tree(fruit_tree)

if __name__ == "__main__":
    main()
