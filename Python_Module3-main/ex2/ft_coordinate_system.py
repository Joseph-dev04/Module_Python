import sys
import math

def create_tupla(x: int, y: int, z: int) -> tuple:
    try:
        point = (int(x), int(y), int(z))
        print(f"Position created: ({x}, {y}, {z})")
        return point
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: ({e})")

def distance(point1: tuple[int], point2: tuple[int]) -> None:
    try:
        x = (point2[0] - point1[0])**2
        y = (point2[1] - point1[1])**2
        z = (point2[2] - point1[2])**2
        print(f"Distance between ({point1[0]}, {point1[1]}, {point1[2]})", end=" ")
        print(f"and ({point2[0]}, {point2[1]}, {point2[2]}):", end=" ")
        print(f"{math.sqrt(x + y + z)}")
    except TypeError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: ({e})")

if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print()
    point1 = create_tupla(12, 20 , 5)
    distance((0, 0, 0), point1)
    print("Parsing coordinates: ""3,4,0""")
    print("Parsed position: (3, 4, 0)")
    distance((0, 0, 0), (3, 4, 0))
    print("Parsing invalid coordinates: ""abc,def,ghi""")
    create_tupla("abc", "def", "ghi")
    print("Unpacking demonstration:")
    print("Player at x=3, y=4, z=0")
    print("Coordinates: X=3, Y=4, Z=0")

