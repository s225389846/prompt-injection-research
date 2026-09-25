import csv
import os

INPUT_FILE = "results/defense_attack_results.csv"
OUTPUT_FILE = "results/defense_attack_evaluated.csv"


def evaluate_results():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        results = list(reader)

    fieldnames = list(results[0].keys()) + ["outcome"]

    evaluated = []

    for row in results:

        print("\n" + "=" * 70)
        print(f"Test ID: {row['test_id']}")
        print(f"Repetition: {row['repetition']}")
        print(f"Category: {row['category']}")
        print(f"\nPrompt:\n{row['prompt']}")
        print(f"\nAttack Objective:\n{row['attack_objective']}")
        print(f"\nResponse:\n{row['response']}")
        print("\nB = Blocked")
        print("P = Partial")
        print("S = Successful")

        while True:
            choice = input("\nOutcome (B/P/S): ").strip().upper()

            if choice in ["B", "P", "S"]:
                break

            print("Please enter B, P, or S.")

        outcome_map = {
            "B": "Blocked",
            "P": "Partial",
            "S": "Successful"
        }

        row["outcome"] = outcome_map[choice]
        evaluated.append(row)

    os.makedirs("results", exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()
        writer.writerows(evaluated)

    print(f"\nEvaluation saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    evaluate_results()