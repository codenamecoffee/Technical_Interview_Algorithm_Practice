import os
import random
from pathlib import Path
from datetime import datetime
import time

# --- Configuración ---
BASE_DIR = Path(__file__).parent.parent

CATEGORIES = ["basics", "intermediate", "advanced"]

def countdown_and_lock_files(files, minutes=60):
    total_seconds = minutes * 60
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time left: {timer}", end="")
        time.sleep(1)
    print("\nTime is up! Setting files to read-only...")

    for file_path in files:
        os.chmod(file_path, 0o444)

def extract_docstring(filepath):
    # Extracts the first triple-quoted docstring from a Python file.
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    docstring = []
    inside = False
    for line in lines:
        if '"""' in line:
            if not inside:
                inside = True
                docstring.append(line)
                if line.count('"""') == 2:  # Docstring in one line
                    break
            else:
                docstring.append(line)
                break
        elif inside:
            docstring.append(line)
    return "".join(docstring) if docstring else None

def create_practice_files(selected_exercises) -> list:
    # Step 1: Check if the 'practice' folder exists in the repo root. If not, create it.
    practice_dir = os.path.join(BASE_DIR, "practice")
    if not os.path.exists(practice_dir):
        os.mkdir(practice_dir)

    # Step 2: Create a subfolder named with today's date (YYYY_MM_DD format) inside 'practice'.
    today = datetime.now().strftime("%Y_%m_%d")
    date_dir = os.path.join(practice_dir, today)
    if not os.path.exists(date_dir):
        os.mkdir(date_dir)

    created_files = [] # Save the paths to return them after

    # Step 3: For each selected exercise, create a new file in the date folder.
    # The file name format is: {difficulty}_{original_name}_attempt.py
    for difficulty, filename in selected_exercises.items():
        base_name = filename.replace(".py", "")
        new_filename = f"{difficulty}_{base_name}_attempt.py"
        file_path = os.path.join(date_dir, new_filename)
        created_files.append(file_path)
        # Get the original file path
        original_path = os.path.join(BASE_DIR, difficulty, filename)
        docstring = extract_docstring(original_path)
        with open(file_path, "w", encoding="utf-8") as f:
            if docstring:
                f.write(docstring + "\n\n")
            f.write(f"# Attempt for {filename} ({difficulty})\n\n")

    return created_files

def pick_random_exercise(category: str) -> str:
    """Devuelve un archivo random dentro de una categoría."""
    folder = BASE_DIR / category
    files = [f for f in folder.iterdir() if f.is_file() and f.suffix == ".py"]

    if not files:
        return f"[No hay ejercicios en {category}]"

    return random.choice(files).name


def main():
    print("=" * 40)
    print("🎯  RANDOM PYTHON EXERCISE GENERATOR")
    print("=" * 40)

    selected_exercises = {}

    for cat in CATEGORIES:
        chosen = pick_random_exercise(cat)
        selected_exercises[cat] = chosen
        print(f"- {cat.capitalize()}: {chosen}")

    print("=" * 40)

    created_files = create_practice_files(selected_exercises)

    # Start the timer and lock files after 60 minutes
    countdown_and_lock_files(created_files, minutes=1)

if __name__ == "__main__":
    main()
