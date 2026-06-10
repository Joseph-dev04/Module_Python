if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    print("Initializing new storage unit: new_discovery.txt")
    print("")
    try:
        with open("new_discovery.txt", "x") as f:
            print("Storage unit created successfully...")
            f.write("[ENTRY 001] New quantum algorithm discovered\n")
            f.write("[ENTRY 002] Efficiency increased by 347%\n")
            f.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    except FileExistsError:
        print("ERROR: The file exist")
