import sys

if __name__ == "__main__":
    argc = len(sys.argv)
    print("=== Player Score Analytics ===")
    try:
        if (argc > 1):
            print("Scores processed: [", end="")
            for score in sys.argv[1:argc-1]:
                print(f"{score},", end=" ")
            amount = sum(int(x) for x in sys.argv[1:])
            high = max(int(x) for x in sys.argv[1:])
            low = min( int(x) for x in sys.argv[1:])
            print(f"{sys.argv[argc-1]}]")
            print(f"Total players: {len(sys.argv[1:])}")
            print(f"Total score: {amount}")
            print(f"Average score: {amount / len(sys.argv[1:])}")
            print(f"High score: {high}")
            print(f"Low score: {low}")
            print(f"Score range: {high - low}")
        else:
            print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    except ValueError as e:
        print("]")
        print(f"{e}")