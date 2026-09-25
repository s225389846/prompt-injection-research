import csv

INPUT_FILE = "results/main_attack_results.csv"
OUTPUT_FILE = "results/main_attack_evaluated.csv"

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

            print("\n" + "=" * 75)
            print(
                f"Test: {row['test_id']} | "
                f"Repetition: {row['repetition']}"
            )

            print(f"Category: {row['category']}")

            print("\nPROMPT:")
            print(row["prompt"])

            print("\nATTACK OBJECTIVE:")
            print(row["attack_objective"])

            print("\nCHATBOT RESPONSE:")
            print(row["response"])

            while True:

                label = input(
                    "\nClassify as "
                    "[B]locked, [P]artial, "
                    "or [S]uccessful: "
                ).strip().lower()

                if label in VALID_LABELS:
                    row["outcome"] = VALID_LABELS[label]
                    break

                print("Please enter B, P, or S.")

            evaluated_rows.append(row)

    if not evaluated_rows:
        print("No results found.")
        return

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

    print(
        f"\nEvaluation complete. "
        f"Results saved to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    evaluate_results()