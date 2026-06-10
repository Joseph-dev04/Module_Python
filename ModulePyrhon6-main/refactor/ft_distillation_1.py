import alchemy
from alchemy.potions import healing_potion as heal

if __name__ == "__main__":
	print("=== Distillation 1 ===")
	print("Using: 'import alchemy' structure to access potions")
	print("Testing strength_potion:", end=" ")
	print(alchemy.potions.strength_potion())
	print("Testing heal alias:", end=" ")
	print(heal())