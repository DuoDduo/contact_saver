# Function to read and display participants from the CSV file
def load_participant(csv_file):
    print("\nReading CSV file:")
    if csv_file.exists():
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)  # Read the CSV file row by row
            for row_number, row in enumerate(reader):
                if row_number == 0:  # First row is the header
                    print(f"Headers: {' | '.join(row)}")  # Print headers nicely
                    print("-" * 40)  # Print a line separator
                else: 
                    name, age, phone, track = row
                    print(f"{name} {age} {phone} {track}")  # Print row data in a readable format
    else:
        print("No participants found yet.")