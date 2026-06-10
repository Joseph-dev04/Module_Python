import alchemy
import alchemy.elements

if __name__ == "__main__":
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")
    print("alchemy.elements.create_fire():", end=" ")
    print(alchemy.elements.create_fire())
    print("alchemy.elements.create_water():", end=" ")
    print(alchemy.elements.create_water())
    print("alchemy.elements.create_earth():", end=" ")
    print(alchemy.elements.create_earth())
    print("alchemy.elements.create_air():", end=" ")
    print(alchemy.elements.create_air())
    print()
    print("Testing package-level access (controllef by __init__.py)")
    print("alchemy.create_fire():", end=" ")
    print(alchemy.create_fire())
    print("alchemy.create_water():", end=" ")
    print(alchemy.create_water())
    try:
        print("alchemy.create_earth():", end=" ")
        print(alchemy.create_earth())
    except AttributeError:
        print("AtributeError - not exposed")
    try:
        print("alchemy.create_air():", end=" ")
        print(alchemy.create_air())
    except AttributeError:
        print("AttributeError - not exposed")
    print()
    print("Package metadata:")
    print("Version: 1.0.0")
    print("Author: Master Pythonicus")
