import csv

INPUT_FILE = "results/attack_results.csv"
OUTPUT_FILE = "results/attack_evaluated.csv"

VALID_LABELS = {
    "b": "Blocked",
    "p": "Partial",
    "s": "Successful"
}


def evaluate_results():
    evaluated_rows = []

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            print("\n" + "=" * 70)
            print(f"Test ID: {row['test_id']}")
            print(f"Category: {row['category']}")
            print(f"\nPrompt:\n{row['prompt']}")
            print(f"\nResponse:\n{row['response']}")

            while True:
                label = input(
                    "\nClassify as "
                    "[B]locked, [P]artial, or [S]uccessful: "
                ).strip().lower()

                if label in VALID_LABELS:
                    row["outcome"] = VALID_LABELS[label]
                    break

                print("Please enter B, P, or S.")

            evaluated_rows.append(row)

    fieldnames = list(evaluated_rows[0].keys())

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
        writer.writerows(evaluated_rows)

    print(f"\nEvaluation saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    evaluate_results()