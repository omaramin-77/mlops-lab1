import os
import sys
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    student_name = os.getenv("NAME", "Unknown")
    student_id = os.getenv("ID", "Unknown")

    if len(sys.argv) > 1:
        csv_path = Path(sys.argv[1])
    else:
        csv_path = Path(input("Enter the path to your CSV file: ").strip())

    if not csv_path.is_file():
        print(f"Error: file not found: {csv_path}")
        sys.exit(1)

    if csv_path.suffix.lower() != ".csv":
        print("Error: please provide a .csv file.")
        sys.exit(1)

    try:
        df = pd.read_csv(csv_path)
    except Exception as exc:
        print(f"Error reading CSV file: {exc}")
        sys.exit(1)

    print(f"Student: {student_name}")
    print(f"ID: {student_id}")
    print(f"File: {csv_path}")

    print("\nFirst three rows:")
    print(df.head(3).to_string(index=False))


if __name__ == "__main__":
    main()