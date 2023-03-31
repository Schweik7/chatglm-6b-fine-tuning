import json
import csv
from pathlib import Path

# Define the input and output directories
input_dir = Path("psy_data_raw")
output_dir = Path("psy_data")

# Loop through all csv files in the input directory
for csv_file in input_dir.glob("*.csv"):
    # Open the csv file and create a csv_reader
    with open(csv_file, "r", encoding="gb18030") as f:
        csv_reader = csv.DictReader(f, fieldnames=["instruction", "input", "output"])
        # Create a list to store the rows
        rows = []
        # Loop through each row in the csv_reader
        for row in csv_reader:
            # Append the row to the list
            rows.append(row)
        # Create the output filename by replacing the directory name
        output_filename = csv_file.name.replace(input_dir.name, output_dir.name)
        # Open the output file and write the rows in json format
        with open(output_dir / output_filename, "w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=4)
