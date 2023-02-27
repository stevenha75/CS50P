import sys
import csv


def main():
    # Check command line arguments
    check_cl_args()

    # Output List (List of dicts)
    output = []

    # Check for valid file
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            # storing first, last, and house for each row as a dict
            for row in reader:
                last, first = row["name"].split(",")
                output.append(
                    {"first": first.lstrip(), "last": last, "house": row["house"]}
                )
    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")

    # Writing into a new csv
    with open(sys.argv[2], "w") as file:
        fields = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        for row in output:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )


def check_cl_args():
    # Expect two CL args
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()
