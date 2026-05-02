from pathlib import Path
import csv

folder = Path.home() / "Documents" / "Activity_5_Files"

results = []

for file in folder.glob("*.txt"):
    text = file.read_text()
    lines = [line for line in text.splitlines() if line.strip()]
    words = text.split()
    chars = len(text)

    line_count = len(lines)
    word_count = len(words)

    wpl = word_count / line_count if line_count else 0
    cpw = chars / word_count if word_count else 0

    results.append([file.name, line_count, word_count, chars, round(wpl,2), round(cpw,2)])

# Sort by word density (words per line)
results.sort(key=lambda x: x[4], reverse=True)

# Display
print("Filename | Lines | Words | Characters | Words/Line | Chars/Word")
for r in results:
    print(r)

# Export to CSV
csv_file = folder / "content_summary.csv"
with csv_file.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Filename","Lines","Words","Characters","Words/Line","Chars/Word"])
    writer.writerows(results)

print("\nMost dense file:", results[0][0])
print("Least dense file:", results[-1][0])

from pathlib import Path
import string
from collections import Counter

folder = Path.home() / "Documents" / "Activity_5_Files"

# Load stopwords (optional)
stopwords_file = folder / "stopwords.txt"
stopwords = set()

if stopwords_file.exists():
    stopwords = set(stopwords_file.read_text().split())

word_counts = Counter()

for file in folder.glob("*.txt"):
    text = file.read_text().lower()

    # remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    words = text.split()

    filtered = [w for w in words if w not in stopwords]
    word_counts.update(filtered)

# Show top words
print("Most frequent words:")
for word, count in word_counts.most_common(10):
    print(word, ":", count)

from pathlib import Path
from datetime import datetime
import shutil

student_id = "2025-0204"
student_name = "Jhon Martin Duat"

source_folder = Path.home() / "Documents" / "Activity_5_Exercises"
backup_folder = source_folder / f"backup_{student_id}"
backup_folder.mkdir(parents=True, exist_ok=True)

file_to_backup = source_folder / "sample.txt"

if file_to_backup.exists():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    backup_name = f"{file_to_backup.stem}_{student_id}_{timestamp}{file_to_backup.suffix}"
    backup_path = backup_folder / backup_name

    shutil.copy(file_to_backup, backup_path)

    size = file_to_backup.stat().st_size

    log_file = backup_folder / f"backup_log_{student_id}.txt"

    with log_file.open("a") as log:
        log.write(f"{student_id} - {student_name}\n")
        log.write(f"File: {file_to_backup.name}\n")
        log.write(f"Time: {timestamp}\n")
        log.write(f"Size: {size} bytes\n")
        log.write(f"Backup Path: {backup_path}\n")
        log.write("-"*30 + "\n")

    print(f"Backup completed for {student_id} ({student_name})")
    print(f"File saved as: {backup_name}")
    print(f"Log updated at: {backup_folder}")
else:
    print("File not found.")

    file_to_backup = source_folder / "sample.txt"

# Create file if it doesn't exist
if not file_to_backup.exists():
    file_to_backup.write_text("This is a sample file for backup.")
    print("Sample file created.")

# Continue backup
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")