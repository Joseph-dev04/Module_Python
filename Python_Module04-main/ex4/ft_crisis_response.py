def file_open(resource: str) -> None:
    try:
        print(f"CRISIS ALERT: Attempting access to '{resource}'...")
        with open(resource, "r") as f:
            print("SUCCESS: Archive recovered:", end=" ")
            for line in f:
                print(line, end="")
            print()
            print("STATUS: Normal operations resumed")
        print()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    file_open("../lost_archive.txt")
    file_open("../classified_data.txt")
    file_open("../standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")
