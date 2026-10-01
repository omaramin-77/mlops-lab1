import os
import sys

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

file = sys.argv[1] if len(sys.argv) > 1 else input("Enter CSV file path: ")

df = pd.read_csv(file)

print("Name:", os.getenv("NAME"))
print("ID:", os.getenv("ID"))
print("\nFirst 3 rows:")
print(df.head(3))