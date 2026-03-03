from alchemy import transmutation
import alchemy.transmutation


if __name__ == "__main__":
    try:

        print("=== Pathway Debate Mastery ===\n")

        print("Testing Absolute Imports (from basic.py):")
        print(f"lead_to_gold(): {transmutation.lead_to_gold()}")
        print(f"stone_to_gem(): {transmutation.stone_to_gem()}")

        print("\nTesting Relative Imports (from advanced.py):")
        print(f"philosophers_stone(): {transmutation.philosophers_stone()}")
        print(f"elixir_of_life(): {transmutation.elixir_of_life()}")

        print("Testing Package Access:")
        print("alchemy.transmutation.lead_to_gold(): "
              f"{alchemy.transmutation.lead_to_gold():}")
        print("alchemy.transmutation.philosophers_stone(): "
              f"{alchemy.transmutation.philosophers_stone():}")

        print("\nBoth pathways work! Absolute: clear, Relative: concise")
    except Exception as e:
        print(e)
