
if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    print()
    alice_colec = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob_colec = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie_colec = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice_colec}")
    print(f"Player bob achievements: {alice_colec}")
    print(f"Player charlie achievements: {alice_colec}")
    print()
    print("=== Achievement Analytics ===")
    collection = set.union(alice_colec, bob_colec, charlie_colec)
    print(f"All unique achievements: {collection}")
    print(f"Total unique achievements: {len(collection)}")
    unique = set.union(alice_colec, bob_colec, charlie_colec)
    print(f"Common to all players: {unique}")
    rare = set.intersection(alice_colec, bob_colec, charlie_colec)
    print(f"Rare achievements (1 player): {rare}")
    print()
    print(f"Alice vs Bob common: {set.intersection(alice_colec, bob_colec)}")
    print(f"Alice unique: {set.difference(alice_colec, bob_colec)}")
    print(f"Bob unique: {set.difference(bob_colec, alice_colec)}")
    