import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    id = input("Input Stream active. Enter archivist ID: ")
    message = input("Input Stream active. Enter status report:")
    print()
    print(f"[STANDARD] Archive status from {id}: {message}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful.")
