import csv
from collections import Counter, defaultdict

INPUT_FILE = "results/main_attack_evaluated.csv"


def analyse_results():
    outcomes = []
    categories = defaultdict(list)
    tests = defaultdict(list)

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            outcome = row["outcome"]
            category = row["category"]
            test_id = row["test_id"]

            outcomes.append(outcome)
            categories[category].append(outcome)
            tests[test_id].append(outcome)

    total = len(outcomes)
    counts = Counter(outcomes)

    blocked = counts.get("Blocked", 0)
    partial = counts.get("Partial", 0)
    successful = counts.get("Successful", 0)

    asr = (successful / total) * 100 if total else 0

    print("\n========== OVERALL PRE-DEFENCE RESULTS ==========")
    print(f"Total observations: {total}")
    print(f"Blocked: {blocked} ({blocked/total*100:.2f}%)")
    print(f"Partial: {partial} ({partial/total*100:.2f}%)")
    print(
        f"Successful: {successful} "
        f"({successful/total*100:.2f}%)"
    )
    print(f"Strict Attack Success Rate (ASR): {asr:.2f}%")

    print("\n========== RESULTS BY CATEGORY ==========")

    for category, results in categories.items():
        category_total = len(results)
        category_counts = Counter(results)

        b = category_counts.get("Blocked", 0)
        p = category_counts.get("Partial", 0)
        s = category_counts.get("Successful", 0)

        category_asr = (s / category_total) * 100

        print(f"\n{category}")
        print(f"Total: {category_total}")
        print(f"Blocked: {b}")
        print(f"Partial: {p}")
        print(f"Successful: {s}")
        print(f"ASR: {category_asr:.2f}%")

    print("\n========== RESULTS BY TEST ==========")

    for test_id, results in tests.items():
        test_counts = Counter(results)

        print(
            f"{test_id}: "
            f"B={test_counts.get('Blocked', 0)}, "
            f"P={test_counts.get('Partial', 0)}, "
            f"S={test_counts.get('Successful', 0)}"
        )


if __name__ == "__main__":
    analyse_results()