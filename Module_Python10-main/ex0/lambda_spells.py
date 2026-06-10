#Sort artifacts by power (descending)
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


#Filter mages by minimum power
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


#Transform spell names
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


#Calculate mage statistics
def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda m: m["power"])["power"]
    min_power = min(mages, key=lambda m: m["power"])["power"]
    avg_power = round(sum(map(lambda m: m["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


#Demo
def main():
    artifacts = [
        {"name": "Fire Staff", "power": 92, "type": "fire"},
        {"name": "Crystal Orb", "power": 85, "type": "arcane"},
        {"name": "Shadow Blade", "power": 78, "type": "dark"},
    ]

    mages = [
        {"name": "Aldor", "power": 95, "element": "fire"},
        {"name": "Lyra", "power": 70, "element": "water"},
        {"name": "Zane", "power": 88, "element": "air"},
    ]

    spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power) "
        f"comes before {sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(" ".join(transformed))

    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(stats)


if __name__ == "__main__":
    main()