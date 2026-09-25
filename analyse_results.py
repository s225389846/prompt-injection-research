import csv
from collections import Counter, defaultdict

INPUT_FILE = "results/attack_evaluated.csv"


def analyse_results():
    outcomes = []
    categories = defaultdict(list)

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            outcome = row["outcome"]
            category = row["category"]

            outcomes.append(outcome)
            categories[category].append(outcome)

    total = len(outcomes)
    counts = Counter(outcomes)

    successful = counts.get("Successful", 0)
    partial = counts.get("Partial", 0)
    blocked = counts.get("Blocked", 0)

    asr = (successful / total) * 100 if total else 0

    print("\n=== OVERALL RESULTS ===")
    print(f"Total attacks: {total}")
    print(f"Blocked: {blocked}")
    print(f"Partial: {partial}")
    print(f"Successful: {successful}")
    print(f"Attack Success Rate: {asr:.2f}%")

    print("\n=== RESULTS BY ATTACK CATEGORY ===")

    for category, results in categories.items():
        category_total = len(results)
        category_counts = Counter(results)

        category_successful = category_counts.get(
            "Successful", 0
        )

        category_asr = (
            category_successful / category_total
        ) * 100

        print(f"\n{category}")
        print(f"Tests: {category_total}")
        print(
            f"Blocked: "
            f"{category_counts.get('Blocked', 0)}"
        )
        print(
            f"Partial: "
            f"{category_counts.get('Partial', 0)}"
        )
        print(
            f"Successful: {category_successful}"
        )
        print(f"ASR: {category_asr:.2f}%")


if __name__ == "__main__":
    analyse_results()