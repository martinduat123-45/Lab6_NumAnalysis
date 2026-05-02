# WRITING TO A FILE
from pathlib import Path

# Define a custom folder in your Documents directory
output_dir = Path.home() / "Documents" / "Duat_Activity_5"
output_dir.mkdir(exist_ok=True)  # Creates folder if missing

# Define the file path
file_path = output_dir / "Act5_example.txt"

# Write text to the file
with open(file_path, "w", encoding="utf-8") as file:
    file.write("Hello, Welcome to Python Programming!\n")
    file.write("File saved safely with pathlib.\n")
    file.write("Python makes file handling easy!")

# Confirm that the file is saved
print(f"File saved to: {file_path.resolve()}")

# Step 1: Read the entire file content if it exists
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:\n", content)

# Step 2: Read line-by-line
with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, 1):
        clean_line = line.strip()
        
        if "Python" in clean_line:
            print(f"Line {line_number}: {clean_line}")

            word_count = len(clean_line.split())
            print(f"   Word count: {word_count}")

 # Step 1: Open file in append mode
with open(file_path, "a", encoding="utf-8") as file:
    file.write("\nThis line was added!")

# Step 2: Confirm that data was added
print("Data appended successfully.")

# Append multiple lines using a list and writelines()
lines = [
    "\nSecond line added.",
    "\nThird line added.",
    "\nFourth line added."
]

with open(file_path, "a", encoding="utf-8") as file:
    file.writelines(lines)

print("Multiple lines appended successfully.")

# Ask the user for input and append it to the file
user_input = input("Enter a line to add: ")

with open(file_path, "a", encoding="utf-8") as file:
    file.write("\n" + user_input)

print("User input appended successfully.")

from pathlib import Path
from datetime import datetime
import shutil

# Change to your surname
SURNAME = "Duat"

# Step 2: Define working directory
backup_dir = Path.home() / "Documents" / f"{SURNAME}_Activity_5"
backup_dir.mkdir(exist_ok=True)

# Let user choose overwrite or append
def write_with_backup(filename: str, content: str, mode="w"):
    file_path = backup_dir / filename

    # Create backup if file exists
    if file_path.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = file_path.with_name(
            f"{file_path.stem}_{SURNAME}_backup_{timestamp}{file_path.suffix}"
        )
        shutil.copy2(file_path, backup_path)
        print(f"Backup saved: {backup_path.name}")

    # Write or append based on mode
    with open(file_path, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n" + content)
        else:
            file.write(content)

    print(f"File saved: {file_path.name}")

# Step 4: Read file function
def read_file(filename: str):
    file_path = backup_dir / filename
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# List backups for a specific file
def list_backups(filename: str):
    print("\nBackups for", filename)
    for backup in backup_dir.glob(f"{Path(filename).stem}_*backup*"):
        print("-", backup.name)

# Step 5: Run demo
print("=== File Operations Demo ===")

print("\n1. Creating new file:")
write_with_backup("demo.txt", "Initial content", "w")

print("\n2. Updating file (with backup):")
write_with_backup("demo.txt", "Updated content", "w")

print("\n3. Appending content (user choice):")
write_with_backup("demo.txt", "Appended content", "a")

print("\n4. Reading file:")
print(read_file("demo.txt"))

print("\n5. Listing backups:")
list_backups("demo.txt")

from pathlib import Path
from datetime import datetime
import shutil

# Add your surname
SURNAME = "Duat"

# Change working directory
backup_dir = Path.home() / "Documents" / f"{SURNAME}_Activity_5"
backup_dir.mkdir(exist_ok=True)

# Menu-driven file manager
def file_manager():
    file_name = input("Enter filename (e.g., notes.txt): ")
    file_path = backup_dir / file_name

    while True:
        print("\n--- MENU ---")
        print("1. Write to file")
        print("2. Append to file")
        print("3. Read file")
        print("4. Backup file")
        print("5. Exit")
        print("6. List backups")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            content = input("Enter content to write:\n")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print("File written successfully.")

        elif choice == "2":
            more = input("Enter content to append:\n")
            with open(file_path, "a", encoding="utf-8") as f:
                f.write("\n" + more)
            print("Content appended.")

        elif choice == "3":
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    print("\nFile Content:\n", f.read())
            else:
                print("File not found.")

        elif choice == "4":
            if file_path.exists():
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                backup_file = file_path.with_name(
                    f"{file_path.stem}_{SURNAME}_backup_{timestamp}{file_path.suffix}"
                )
                shutil.copy2(file_path, backup_file)
                print(f"Backup created: {backup_file.name}")
            else:
                print("Cannot backup. File does not exist.")

        elif choice == "5":
            print("Exiting the file manager.")
            break

        elif choice == "6":
            print("\nBackup files:")
            backups = list(backup_dir.glob(f"{file_path.stem}_{SURNAME}_backup_*"))
            if backups:
                for b in backups:
                    print("-", b.name)
            else:
                print("No backups found.")

        else:
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    file_manager()