def obtener_puntuacion(jugador):
    return jugador["score"]


def main():
    data = [
        {"player": "alice", "score": 2300, "achievements":
         ["first_kill", "level_10"], "region": "north", "active": True},
        {"player": "bob", "score": 1800, "achievements": ["level_10"],
         "region": "east", "active": True},
        {"player": "charlie", "score": 2150, "achievements":
         ["first_kill", "boss_slayer"], "region": "north", "active": True},
        {"player": "diana", "score": 2050, "achievements":
         ["boss_slayer", "marathoner"], "region": "central", "active": False}
    ]
    print("=== Game Analytics Dashboard ===")
    high_scorers = [d["player"] for d in data if d["score"] > 2000]
    scores_doubled = [d["score"] * 2 for d in data]
    active_players = [d["player"] for d in data if d["active"] is True]

    print("\n=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")

    player_scores = {d["player"]: d["score"]
                     for d in data if d["active"] is True}
    score_categories = {d["player"]: ("high" if d["score"] > 2000 else "low")
                        for d in data}
    achievement_counts = {d["player"]: len(d["achievements"]) for d in data}

    print("\n=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")

    unique_players = {d["player"] for d in data}
    unique_regions = {d["region"] for d in data}
    all_achievements = {ach for d in data for ach in d["achievements"]}

    print("\n=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {all_achievements}")
    print(f"Active regions: {unique_regions}")

    total_scores = [d["score"] for d in data]
    avg_score = sum(total_scores) / len(total_scores)
    top_player = sorted(data, key=obtener_puntuacion)[-1]

    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(all_achievements)}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top_player['player']}", end=" ")
    print(f"({top_player['score']} points,", end=" ")
    print(f"{achievement_counts.get(top_player['player'])} achievements)")


if __name__ == "__main__":
    main()
