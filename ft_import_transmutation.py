import alchemy.elements
import alchemy.potions
from alchemy.elements import create_fire, create_water, create_earth
from alchemy.potions import healing_potion as heal

if __name__ == "__main__":
    try:
        print("=== Import Transmutation Mastery ===\n")

        print("Method 1 - Full module import:")
        print("alchemy.elements.create_fire():"
              f"{alchemy.elements.create_fire()}")

        print("\nMethod 2 - Specific function import:")
        print(f"create_water(): {create_water()}")

        print("\nMethod 3 - Aliased import:")
        print(f"heal(): {heal()}")

        print("\nMethod 4 - Multiple imports:")
        print(f"create_earth(): {create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {alchemy.potions.strength_potion()}")

        print("\nAll import transmutation methods mastered!")
    except Exception as e:
        print(e)
