
if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    print("Connection established...")
    print()
    try:
        with open("../ancient_fragment.txt") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print("File not found: ancient_fragment.txt")
    except PermissionError:
        print("permission deneged: ancient_fragment.txt")
