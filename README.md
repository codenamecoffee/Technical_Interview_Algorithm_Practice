# Technical Interview Algorithm Practice

This repository contains my ongoing training for technical interviews, focused on algorithmic thinking, Python problem-solving, and coding efficiency.

The goal is to strengthen my ability to solve problems under constraints — time pressure, limited tools, and no external help — replicating real interview conditions.

<br>

## 📁 Repository Structure

- basics/ → Fundamental exercises (strings, arrays, loops, conditionals)
- intermediate/ → Problems requiring data structures and multi-step logic
- advanced/ → Complex problems involving recursion, optimization, or custom algorithms
- random_challenge/ → Script that generates 3 random exercises (basic, intermediate, advanced)

<br>

## 🎯 Training Strategy

1. **Day A – Learning New Problems (Hackerrank / LeetCode style)**
   - Study 1–3 new exercises.
   - Write a clean, well-documented solution in Python.
   - Add comments explaining:
     - core logic
     - edge cases
     - time & space complexity

<br>

2. **Day B – Random Challenge (Interview Simulation)**
   - Run the `generator.py` script.
   - Solve 3 random problems:
     - 1 basic  
     - 1 intermediate  
     - 1 advanced  
   - No external help (AI, internet, notes).
   - Timer on → real interview pressure.
   - Document results if needed.

<br>

## 🧪 Random Challenge Script

Located in: `random_challenge/generator.py`

This script automatically selects one random exercise from each difficulty level (basics, intermediate, advanced) to simulate unpredictable and realistic interview practice sessions.

- Creates a `practice` folder in the repository root (if it doesn't exist).
- Inside `practice`, generates a subfolder named with the current date (`YYYY_MM_DD`).
- Copies the selected exercises' problem descriptions (docstrings) into new attempt files, named by difficulty and exercise, e.g.:
  - `basic_exercise_009_find_min_and_max_attempt.py`
  - `intermediate_exercise_002_character_compression_attempt.py`
  - `advanced_exercise_002_longest_unique_substring_attempt.py`
- All attempt files are placed in the dated subfolder for easy organization.
- Starts a 60-minute countdown timer in the terminal. When time is up, all attempt files are set to read-only mode to simulate real interview pressure.
- The timer and file locking can be customized for shorter or longer sessions.

This workflow helps you practice under realistic constraints, track your daily progress, and keep your solutions organized.

<br>

## 📌 Purpose of This Repository

Technical interviews require:
- algorithmic fluency 
- strong reasoning skills  
- performance under pressure  
- clean code and clear logic

This repository is my structured approach to developing those skills over time.
I will continuously update it as I prepare for future opportunities.

<br>

## 📝 License

This project is licensed under the **MIT License**, allowing open usage while keeping authorship intact.
