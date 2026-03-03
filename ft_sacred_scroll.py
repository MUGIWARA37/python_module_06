import alchemy
import alchemy.elements

if __name__ == "__main__":
    try:
        print("=== Sacred Scroll Mastery ===\n")
        print("Testing direct module access:")
        print("alchemy.elements.create_fire():"
              f"{alchemy.elements.create_fire()}")
        print("alchemy.elements.create_fire():"
              f"{alchemy.elements.create_water()}")
        print("alchemy.elements.create_fire():"
              f"{alchemy.elements.create_earth()}")
        print("alchemy.elements.create_fire():"
              f"{alchemy.elements.create_air()}")

        print("\nTesting package-level access (controlled by __init__.py):")
        print("Testing direct module access:")
        print(f"alchemy.elements.create_fire(): {alchemy.create_fire()}")
        print(f"alchemy.elements.create_fire(): {alchemy.create_water()}")

        try:
            print("alchemy.elements.create_fire():"
                  f"{alchemy.create_earth()}")
        except Exception:
            print("alchemy.create_earth(): AttributeError - not exposed")
        try:
            print("alchemy.elements.create_fire():"
                  f"{alchemy.create_air()}")
        except Exception:
            print("alchemy.create_air(): AttributeError - not exposed")

        print("\nPackage metadata:")
        print(f"Version: {alchemy.__version__}")
        print(f"Author: {alchemy.__author__}")
    except Exception as e:
        print(e)
