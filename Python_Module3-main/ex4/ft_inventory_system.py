import sys

def count_values(data: list) -> int:
    count = 0
    for i in data:
        count += int(i)
    return count

def get_inventory(dicc: dict) -> None:
    for key, value in dicc.items():
        print(f"{key} {value} units {100/(count_values(dicc.values())/int(value))}")

def get_abundant(dicc: dict) -> None:
    max = 0
    key_max = ""
    minus = 0
    key_minus = ""
    for key, value in dicc.items():
        if max < int(value):
            max = int(value)
            key_max = key
        if minus == 0:
            minus = int(value)
            key_minus = key
        elif minus > int(value):
            minus = int(value)
            key_minus = key
    print(f"Most abundant: {key_max} ({max} units)")
    print(f"Least abundant: {key_minus} ({minus} units)")

def get_stock(dicc: dict) -> None:
    print("Restock needed: ", end="")
    for key, value in dicc.items():
        if int(value) == 0:
            print(f"{key}",end=" ")
    print()

def get_item(dicc: dict, name: str) -> None:
    if name in dicc:
        print(f"Sample lookup - '{name}' in inventory: True")
    else:
        print("nothing")


if __name__ == "__main__":
    dicc = {}
    for arg in sys.argv[1:]:
        i = 0
        for c in arg:
            i+=1
            if c == ":":
                break
        dicc[arg[:i-1]] = arg[i:]
    print(f"{dicc}")
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {count_values(dicc.values())}")
    print(f"Unique item types: {len(dicc.keys())}")
    print()
    print("=== Current Inventory ===")
    get_inventory(dicc)
    print()
    print("=== Inventory Statistics ===")
    get_abundant(dicc)
    print()
    print("=== Item Categories ===")
    print("Moderate: {'potion':", end=" ")
    print(dicc.pop('potion', 'No encontrado'), '}')
    dicc.pop('potion', 'No encontrado')
    print(f"Scarce: {dicc}")
    print()
    print("=== Management Suggestions ===")
    dicc.update({"sword": 0, "helmet": 0})
    get_stock(dicc)
    print()
    print("=== Dictionary Properties Demo ===")
    dicc.update({"sword": 1, "helmet": 1, "potion": 5})
    print("Dictionary keys:", end=" ")
    print(*dicc.keys())
    print("Dictionary values:", end=" ")
    print(*dicc.values())
    get_item(dicc, 'sword')
