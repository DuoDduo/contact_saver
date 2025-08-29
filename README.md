# 📇 ContactSave

**ContactSaveWre** is a Python-based command-line tool for storing and managing contact information. Users can input participant details (name, age, phone number, track), and the application validates each input before saving it into a structured CSV file. It is designed to be simple, clear, and reliable for basic contact collection tasks.

---

## 🚀 Features

- Collect participant information (Name, Age, Phone Number, Track)
- Strong input validation to ensure data quality
- Automatically creates the workspace folder and CSV file if they don’t exist
- Stores contact details in a structured CSV file
- Allows multiple entries in a session
- Displays a summary of saved contacts

---

## 👨‍💻 Contributors & Contributions

### 🧑‍💻 **James Blessing**  
**Role:** Input Validation & User Interaction  
- Implemented input functions: `get_name()`, `get_age()`, `get_phone()`, `get_track()`  
- Ensured robust validation for all inputs (e.g., no empty names, phone must be 11 digits, etc.)  
- Handled exceptions with user-friendly error messages  
- Ensured data integrity before saving

---

### 🧑‍💻 **Nababa Toyeebah**  
**Role:** Contact Display & File Reading  
- Developed `load_participant()` function to read and display contacts from the CSV  
- Included clean formatting for headers and entries  
- Handled file existence checks and displayed fallback messages if no data is found

---

### 🧑‍💻 **Osho Ridwanullah**  
**Role:** CSV File Writing & Storage Logic  
- Created `save_participant()` to write contact dictionaries to the CSV file  
- Managed auto-creation of the `workspace/` folder if it didn’t exist  
- Ensured headers were added when the file was first created  
- Supported both single and multiple entries in one run

---

### 🧑‍💻 **Fagbayi Kanyinsola**  
**Role:** Program Integration & Control Flow  
- Wrote the main execution logic in `main.py`  
- Integrated input and file operations into a smooth user flow  
- Allowed users to add multiple contacts in one session  
- Displayed a summary after the session ends by loading from the CSV

---

## 🧠 Input Validation Example

If a user enters:
```text
Enter your age: abc
```
#Folder Structure
contact_saver/
│
├── main.py
├── contact_main.py
├── file_op.py
├── file_ops.py
├── README.md
└── workspace/
    └── contacts.csv  # Auto-generated

# Clone the repo
git clone https://github.com/DuoDduo/contact_saver.git
cd contact_saver

# Run the program
python main.py

