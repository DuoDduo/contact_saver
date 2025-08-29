import csv
from pathlib import Path

# Define the folder to store the CSV file
workspace = Path("workspace")
csv_file = workspace / "contacts.csv"  # Path to the CSV file
workspace.mkdir(exist_ok=True)  # Create folder if it doesn't exist

# Define the column names for the CSV file
fieldnames = ["Name", "Age", "Phone", "Track"]


# Function to save participant(s) into the CSV file
def save_participant(csv_file, participant):
    # Convert dictionary of participant to a list
    if type(participant) == dict:
     participant = [participant]
    # If the file already exists, append new data
    if csv_file.exists():
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writerows(participant)
    else:
        # If file doesn't exist, create it and write header first
        print(f"File {csv_file} doesn't exist, Creating it now!")
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(participant)

print("Particicpant data written to CSV file!")