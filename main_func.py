import csv
import file_op
import file_ops
from contact_main import get_name, get_age, get_phone, get_track
from pathlib import Path

# Define the workspace and CSV file path
workspace = Path("workspace")
csv_file = workspace / "contacts.csv"


def main():
    while True:
        try:
            name = get_name()
            age = get_age()
            phone = get_phone()
            track = get_track()

            particicant = {"Name": name, "Age": age, "Phone": phone, "Track": track}

            try:
                file_op.save_participant(csv_file, particicant)
                print("Data written to csv file!")

                update_participant = input("Do you want to add another contact? Yes or No: ")
                if update_participant == "no":
                    print("Saved contact")
                    file_ops.load_participant(csv_file)
            except Exception:
                print("Unexpected error encountered while loading the contact")
        except Exception as e:
            print("Unexpected error:", e) 


if __name__ == "__main__":
     main()
