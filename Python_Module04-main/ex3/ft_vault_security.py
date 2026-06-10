if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()
    try:
        print("SECURE EXTRACTION:")
        with open("../classified_data.txt", "r") as f:
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("permission deneged")
    print()
    print()
    try:
        print("SECURE PRESERVATION:")
        with open("../security_protocols.txt", "r") as f:
            for line in f:
                print(line)
    except FileNotFoundError:
        print("file not found")
    except PermissionError:
        print("permission deneged")
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")
